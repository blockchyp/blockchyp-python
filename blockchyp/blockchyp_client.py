"""
The BlockChyp Client
"""


from datetime import datetime

import requests

from .blockchyp_crypto import CryptoUtils

GATEWAY_HOST = "https://api.blockchyp.com" # live server
TEST_GATEWAY_HOST = "https://test.dev.blockchyp.com" # test server
MS_PER_SECOND = 1000
MS_PER_MINUTE = 60000

class BlockChypClient:
    """
    Provides integration with the BlockChyp gateway and payment terminals for python developers
    """
    def __init__(self, creds, https=False, test=False):
        self.credentials = creds
        self.https = https
        self.route_cache_ttl = 60
        self.default_timeout = 60
        self._route_cache = {}
        self.test = test

    def tokenize(self, public_key, card):
        """
        Creates a token and stores it in the token vault.
        """

    def heartbeat(self):
        """
        Checks for access to the gateway.
        """
        reply = self.__gateway_get("/heartbeat")
        return reply.json()

    def enroll(self, auth_request):
        """
        Collects a payment method and enrolls it in the token vault without authorization.
        """

    def ping(self, terminal):
        """
        Tests connectivity with a terminal.
        """
        route = self.__resolve_terminal_route(terminal)
        reply = self.__terminal_post(route, "/test", payload={"terminalName": terminal})

        return reply.json()

    def charge(self, auth_request):
        """
        This is a direct capture transaction in which a transaction is authorized
        and captured in a single step. Most common.
        """

    def return_validation_error(self, desc):
        """
        Returns an error if validation fails.
        """

    def validate_request(self, request):
        """
        Validates a request.
        """

    def validate_currency(self, val):
        """
        Validates the entered currency and amount.
        """

    def capture(self, request):
        """
        Captures a previously authorized pre-authorization. (Did that sound repetitive?)
        """

    def void(self, request):
        """
        Cancels a pre-authorization.
        """

    def close_batch(self, request):
        """
        Closes the current batch. (Not required if batches auto close.)
        """

    def gift_activate(self, request):
        """
        Activates or recharges a BlockChyp gift card. (Terminal Only).
        """

    def refund(self, auth_request):
        """
        Executes a refund.
        """

    def preauth(self, auth_request):
        """
        This transaction authorizes a card and delays capture.
        Used a lot in hospitality transactions where the final capture amount might be different
        or if regulations require delaying capture until shipment.
        """

    def is_terminal_routed(self, request):
        """
        Checks whether a terminal has a valid route.
        """

    def __gateway_get(self, path):
        if self.test:
            url = TEST_GATEWAY_HOST + "/api" + path
        else:
            url = GATEWAY_HOST + "/api" + path
        if self.credentials and self.credentials["api_key"]:
            crypto = CryptoUtils()
            headers = crypto.generate_gateway_headers(self.credentials)
        else:
            headers = {}
        reply = requests.get(url, headers=headers)

        return reply

    def __gateway_post(self, path, payload):
        pass

    def __terminal_get(self, terminal, path, creds):
        pass

    def __terminal_post(self, route, path, payload=None):
        url = self.__assemble_terminal_url(route, path)
        transient_credentials = route["transientCredentials"]
        request_wrapper = {
            "apiKey": transient_credentials["apiKey"],
            "bearerToken": transient_credentials["bearerToken"],
            "signingKey": transient_credentials["signingKey"],
            "request": payload
        }
        reply = requests.post(url, json=request_wrapper)

        return reply

    def __assemble_terminal_url(self, route, path):
        result = "http"
        if self.https:
            result = result + "s"
        result = result + "://"
        result = result + route["ipAddress"]
        if self.https:
            result = result + ":8443"
        else:
            result = result + ":8080"
        result = result + "/api"
        result = result + path

        return result

    def __resolve_terminal_route(self, terminal_name):
        cache_entry = self._route_cache.get(terminal_name, None)

        if cache_entry:
            # check cache expiration
            if cache_entry.ttl > int(datetime.utcnow().timestamp()) * 1000:
                return cache_entry["route"]

        route_response = self.__gateway_get("/terminal-route?terminal=" + terminal_name)
        route = route_response.json()
        time = int(datetime.utcnow().timestamp()) * 1000
        self._route_cache[terminal_name] = {
            "ttl": time + self.route_cache_ttl * 60000,
            "route": route,
        }

        return route

class BlockChypCredentials:
    """
    Stores the three credential components for easy access
    """
    def __init__(self, api_key, bearer_token, signing_key):
        self.creds = {
            "api_key": api_key,
            "bearer_token": bearer_token,
            "signing_key": signing_key,
        }

    def __getitem__(self, item):
        return self.creds[item]
