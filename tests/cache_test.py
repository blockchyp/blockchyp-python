import io
import json
import os

from blockchyp.cache import TerminalRouteCache

from .util import _tempdir


@_tempdir
def test_online(tempdir):
    """Assert that the cache works in memory."""
    cache = TerminalRouteCache()
    cache.offline_enabled = False
    cache.prefix = tempdir

    route = {"success": True}
    # pylint: disable=protected-access
    cache._cache["foo_bar"] = route

    result = cache.get("bar", {"apiKey": "foo"}, True)

    assert result == route


@_tempdir
def test_expired(tempdir):
    """Assert that expired routes are ignored."""
    cache = TerminalRouteCache()
    cache.offline_enabled = False
    cache.prefix = tempdir

    route = {"success": True}
    # pylint: disable=protected-access
    cache._cache["foo_bar"] = route

    result = cache.get("bar", {"apiKey": "foo"}, False)

    assert result is None


@_tempdir
def test_round_trip(tempdir):
    """Assert that the cache is written to the filesystem and
    can be read back."""
    cache = TerminalRouteCache()
    cache.prefix = tempdir

    credentials = {
        "apiKey": "rootAPIKey",
        "signingKey": b"rootSigningKey".hex(),
        "bearerToken": "rootBearerToken",
    }

    route = {
        "terminalName": "foo",
        "ipAddress": "123.123.123.123",
        "cloudRelayEnabled": False,
        "transientCredentials": {
            "apiKey": "transAPIKey",
            "signingKey": b"transSigningKey".hex(),
            "bearerToken": "transBearerToken",
        },
        "timestamp": "2100-12-20T17:28:22Z",
        "success": True,
    }

    files = os.listdir(tempdir)
    assert len(files) == 0

    cache.put(route, credentials)

    files = os.listdir(tempdir)
    assert len(files) == 1

    for path in files:
        with io.open(os.path.join(tempdir, path)) as f:
            content = json.load(f)

        assert content.get("transientCredentials") != route.get("transientCredentials")

    result = cache.get("foo", credentials)

    assert result == route
