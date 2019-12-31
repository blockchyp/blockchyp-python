import copy
import hashlib
import io
import json
import os
import tempfile
import threading
from datetime import datetime, timedelta
from typing import Optional

from blockchyp import crypto
from blockchyp.util import from_iso_timestamp


class TerminalRouteCache:
    """The terminal route cache speeds up transactions by caching terminal name
    lookups between requests."""

    DEFAULT_PREFIX = os.path.join(tempfile.gettempdir(), ".blockchyp_routes")
    _FIXED_KEY = bytes.fromhex(
        "5005ee6cbc5bc66c9c792ac83305b4c53e37676c715748e2300326017c5e3f02")

    def __init__(self, prefix=DEFAULT_PREFIX):
        self.prefix = prefix
        self._cache = {}
        self.offline_enabled = True
        self.time_to_live = timedelta(hours=1)
        self.lock = threading.Lock()

    def get(self, name, credentials, include_expired=False):
        # type: (str, dict, bool) -> Optional[dict]
        """Check the cache for a terminal route for the given root API key."""

        key = self._to_route_key(name, credentials)
        local_route = self._cache.get(key)
        if local_route and self._valid(local_route, include_expired):
            return local_route

        if self.offline_enabled:
            offline_route = self._get_offline(key, credentials)
            if self._valid(offline_route, include_expired):
                self._cache[key] = offline_route
                return offline_route

        return None

    def put(self, route, credentials):
        # type: (dict, dict) -> None
        """Stores a terminal route for later use."""

        key = self._to_route_key(route["terminalName"], credentials)
        self._cache[key] = route

        if self.offline_enabled:
            self._write(route, credentials)

    def evict(self):
        # type: () -> None
        """Clears the cache. Mainly for testing."""
        self._cache = {}

    def _valid(self, route, include_expired=False):
        # type: (Optional[dict], bool) -> bool
        if not route:
            return False

        if not route.get("success"):
            return False

        return include_expired or self._valid_timestamp(route)

    def _valid_timestamp(self, route):
        # type: (dict) -> bool
        timestamp = route.get("timestamp")
        if not timestamp:
            return False

        try:
            expires = from_iso_timestamp(timestamp) + self.time_to_live
            return expires > datetime.utcnow()
        except ValueError:
            return False

    def _filesystem_path(self, key):
        # type: (str) -> str
        snake_case = key.replace(" ", "_")
        # Not filepath joined to prevent conflicts with the Go SDK.
        return f"{self.prefix}_{snake_case}"

    def _get_offline(self, key, credentials):
        # type: (str, dict) -> Optional[dict]
        content = self._read(key)
        if not content:
            return None

        try:
            content["transientCredentials"] = self._decrypt(
                content.get("transientCredentials"),
                credentials,
            )
        except ValueError:
            return None

        return content

    def _decrypt(self, trans_credentials, root_credentials):
        if not trans_credentials:
            return None

        key = self._offline_key(root_credentials)

        return {
            "apiKey": crypto.decrypt(trans_credentials.get("apiKey"), key),
            "bearerToken": crypto.decrypt(trans_credentials.get("bearerToken"), key),
            "signingKey": crypto.decrypt(trans_credentials.get("signingKey"), key),
        }

    def _encrypt(self, trans_credentials, root_credentials):
        key = self._offline_key(root_credentials)

        return {
            "apiKey": crypto.encrypt(trans_credentials.get("apiKey"), key),
            "bearerToken": crypto.encrypt(trans_credentials.get("bearerToken"), key),
            "signingKey": crypto.encrypt(trans_credentials.get("signingKey"), key),
        }

    def _offline_key(self, credentials):
        key = bytes.fromhex(credentials.get("signingKey"))
        return hashlib.sha256(self._FIXED_KEY + key).digest()

    def _read(self, key):
        path = self._filesystem_path(key)

        self.lock.acquire()
        try:
            if not os.path.isfile(path):
                return None

            with io.open(path) as f:
                try:
                    content = json.load(f)
                    return content
                except json.decoder.JSONDecodeError:
                    os.remove(path)
                    return None
        finally:
            self.lock.release()

        return None


    def _write(self, route, credentials):
        offline_route = copy.deepcopy(route)

        trans_creds = offline_route.get("transientCredentials")
        if not trans_creds:
            return

        offline_route["transientCredentials"] = self._encrypt(
            trans_creds,
            credentials,
        )

        key = self._to_route_key(route["terminalName"], credentials)
        path = self._filesystem_path(key)

        parent = os.path.dirname(path)

        self.lock.acquire()
        try:
            if not os.path.isdir(parent):
                os.makedirs(parent)

            with io.open(path, "w") as f:
                json.dump(offline_route, f)
        finally:
            self.lock.release()

    @staticmethod
    def _to_route_key(name, credentials):
        # type: (str, dict) -> str
        return f"{credentials.get('apiKey')}_{name}"
