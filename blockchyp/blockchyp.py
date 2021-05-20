# Copyright 2019 BlockChyp, Inc. All rights reserved. Use of this code is
# governed by a license that can be found in the LICENSE file.
#
# This file was generated automatically. Changes to this file will be lost every
# time the code is regenerated.
"""
This library allows you to interact with the BlockChyp Terminal and
Gateway APIs.

For more information on this library, see the README.
    https://github.com/blockchyp/blockchyp-python
For more information on the Gateway API, see the docs:
    https://docs.blockchyp.com
"""


import io
import json
import os
import urllib.parse

import requests

from blockchyp import crypto, version
from blockchyp.cache import TerminalRouteCache
from blockchyp.error import BlockChypError
from blockchyp.types import SignatureFormat
from blockchyp.util import iso_timestamp


class Client:
    """The BlockChyp API Client.

    Use this object to interact with BlockChyp Terminals and the Gateway.
    """

    TERMINAL_HTTP_PORT = 8080
    TERMINAL_HTTPS_PORT = 8443

    def __init__(self, api_key, bearer_token, signing_key):
        # type: (str, str, str) -> None
        self.api_key = api_key
        self.bearer_token = bearer_token
        self.signing_key = signing_key

        # Default gateway configuration
        self.gateway_url = "https://api.blockchyp.com"
        self.gateway_test_url = "https://test.blockchyp.com"

        self.gateway_timeout = 20 # Seconds

        # Default terminal configuration
        self.terminal_https = True

        self.terminal_timeout = 60 * 2 # Seconds

        self.internet_session = self._build_session()
        self.terminal_session = self._build_session(crypto.TerminalAdapter())
        self.route_cache = TerminalRouteCache()

    def heartbeat(self, test=False):
        # type: (bool) -> dict
        """Tests connection to the API gateway."""
        return self._gateway_request(
            method="GET",
            path="/api/heartbeat",
            test=test,
        )


    def ping(self, request):
        # type: (dict) -> dict
        """Tests connectivity with a payment terminal."""

        self._populate_signature_options(request)

        if self._is_terminal_routed(request.get("terminalName")):
            response = self._terminal_request(
                method="POST",
                path="/api/test",
                body=request,
                terminal=request.get("terminalName"),
            )
        else:
            response = self._gateway_request(
                method="POST",
                path="/api/terminal-test",
                body=request,
                test=request.get("test", False),
                relay=True,
            )

        self._handle_signature(request, response)

        return response

    def charge(self, request):
        # type: (dict) -> dict
        """Executes a standard direct preauth and capture."""

        self._populate_signature_options(request)

        if self._is_terminal_routed(request.get("terminalName")):
            response = self._terminal_request(
                method="POST",
                path="/api/charge",
                body=request,
                terminal=request.get("terminalName"),
            )
        else:
            response = self._gateway_request(
                method="POST",
                path="/api/charge",
                body=request,
                test=request.get("test", False),
                relay=True,
            )

        self._handle_signature(request, response)

        return response

    def preauth(self, request):
        # type: (dict) -> dict
        """Executes a preauthorization intended to be captured later."""

        self._populate_signature_options(request)

        if self._is_terminal_routed(request.get("terminalName")):
            response = self._terminal_request(
                method="POST",
                path="/api/preauth",
                body=request,
                terminal=request.get("terminalName"),
            )
        else:
            response = self._gateway_request(
                method="POST",
                path="/api/preauth",
                body=request,
                test=request.get("test", False),
                relay=True,
            )

        self._handle_signature(request, response)

        return response

    def refund(self, request):
        # type: (dict) -> dict
        """Executes a refund."""

        self._populate_signature_options(request)

        if self._is_terminal_routed(request.get("terminalName")):
            response = self._terminal_request(
                method="POST",
                path="/api/refund",
                body=request,
                terminal=request.get("terminalName"),
            )
        else:
            response = self._gateway_request(
                method="POST",
                path="/api/refund",
                body=request,
                test=request.get("test", False),
                relay=True,
            )

        self._handle_signature(request, response)

        return response

    def enroll(self, request):
        # type: (dict) -> dict
        """Adds a new payment method to the token vault."""

        self._populate_signature_options(request)

        if self._is_terminal_routed(request.get("terminalName")):
            response = self._terminal_request(
                method="POST",
                path="/api/enroll",
                body=request,
                terminal=request.get("terminalName"),
            )
        else:
            response = self._gateway_request(
                method="POST",
                path="/api/enroll",
                body=request,
                test=request.get("test", False),
                relay=True,
            )

        self._handle_signature(request, response)

        return response

    def gift_activate(self, request):
        # type: (dict) -> dict
        """Activates or recharges a gift card."""

        self._populate_signature_options(request)

        if self._is_terminal_routed(request.get("terminalName")):
            response = self._terminal_request(
                method="POST",
                path="/api/gift-activate",
                body=request,
                terminal=request.get("terminalName"),
            )
        else:
            response = self._gateway_request(
                method="POST",
                path="/api/gift-activate",
                body=request,
                test=request.get("test", False),
                relay=True,
            )

        self._handle_signature(request, response)

        return response

    def balance(self, request):
        # type: (dict) -> dict
        """Checks the remaining balance on a payment method."""

        self._populate_signature_options(request)

        if self._is_terminal_routed(request.get("terminalName")):
            response = self._terminal_request(
                method="POST",
                path="/api/balance",
                body=request,
                terminal=request.get("terminalName"),
            )
        else:
            response = self._gateway_request(
                method="POST",
                path="/api/balance",
                body=request,
                test=request.get("test", False),
                relay=True,
            )

        self._handle_signature(request, response)

        return response

    def clear(self, request):
        # type: (dict) -> dict
        """Clears the line item display and any in progress transaction."""

        self._populate_signature_options(request)

        if self._is_terminal_routed(request.get("terminalName")):
            response = self._terminal_request(
                method="POST",
                path="/api/clear",
                body=request,
                terminal=request.get("terminalName"),
            )
        else:
            response = self._gateway_request(
                method="POST",
                path="/api/terminal-clear",
                body=request,
                test=request.get("test", False),
                relay=True,
            )

        self._handle_signature(request, response)

        return response

    def terminal_status(self, request):
        # type: (dict) -> dict
        """Returns the current status of a terminal."""

        self._populate_signature_options(request)

        if self._is_terminal_routed(request.get("terminalName")):
            response = self._terminal_request(
                method="POST",
                path="/api/terminal-status",
                body=request,
                terminal=request.get("terminalName"),
            )
        else:
            response = self._gateway_request(
                method="POST",
                path="/api/terminal-status",
                body=request,
                test=request.get("test", False),
                relay=True,
            )

        self._handle_signature(request, response)

        return response

    def terms_and_conditions(self, request):
        # type: (dict) -> dict
        """Prompts the user to accept terms and conditions."""

        self._populate_signature_options(request)

        if self._is_terminal_routed(request.get("terminalName")):
            response = self._terminal_request(
                method="POST",
                path="/api/tc",
                body=request,
                terminal=request.get("terminalName"),
            )
        else:
            response = self._gateway_request(
                method="POST",
                path="/api/terminal-tc",
                body=request,
                test=request.get("test", False),
                relay=True,
            )

        self._handle_signature(request, response)

        return response

    def capture_signature(self, request):
        # type: (dict) -> dict
        """Captures and returns a signature."""

        self._populate_signature_options(request)

        if self._is_terminal_routed(request.get("terminalName")):
            response = self._terminal_request(
                method="POST",
                path="/api/capture-signature",
                body=request,
                terminal=request.get("terminalName"),
            )
        else:
            response = self._gateway_request(
                method="POST",
                path="/api/capture-signature",
                body=request,
                test=request.get("test", False),
                relay=True,
            )

        self._handle_signature(request, response)

        return response

    def new_transaction_display(self, request):
        # type: (dict) -> dict
        """Displays a new transaction on the terminal."""

        self._populate_signature_options(request)

        if self._is_terminal_routed(request.get("terminalName")):
            response = self._terminal_request(
                method="POST",
                path="/api/txdisplay",
                body=request,
                terminal=request.get("terminalName"),
            )
        else:
            response = self._gateway_request(
                method="POST",
                path="/api/terminal-txdisplay",
                body=request,
                test=request.get("test", False),
                relay=True,
            )

        self._handle_signature(request, response)

        return response

    def update_transaction_display(self, request):
        # type: (dict) -> dict
        """Appends items to an existing transaction display. Subtotal, Tax, and Total are
        overwritten by the request. Items with the same description are combined into
        groups.
        """

        self._populate_signature_options(request)

        if self._is_terminal_routed(request.get("terminalName")):
            response = self._terminal_request(
                method="PUT",
                path="/api/txdisplay",
                body=request,
                terminal=request.get("terminalName"),
            )
        else:
            response = self._gateway_request(
                method="PUT",
                path="/api/terminal-txdisplay",
                body=request,
                test=request.get("test", False),
                relay=True,
            )

        self._handle_signature(request, response)

        return response

    def message(self, request):
        # type: (dict) -> dict
        """Displays a short message on the terminal."""

        self._populate_signature_options(request)

        if self._is_terminal_routed(request.get("terminalName")):
            response = self._terminal_request(
                method="POST",
                path="/api/message",
                body=request,
                terminal=request.get("terminalName"),
            )
        else:
            response = self._gateway_request(
                method="POST",
                path="/api/message",
                body=request,
                test=request.get("test", False),
                relay=True,
            )

        self._handle_signature(request, response)

        return response

    def boolean_prompt(self, request):
        # type: (dict) -> dict
        """Asks the consumer a yes/no question."""

        self._populate_signature_options(request)

        if self._is_terminal_routed(request.get("terminalName")):
            response = self._terminal_request(
                method="POST",
                path="/api/boolean-prompt",
                body=request,
                terminal=request.get("terminalName"),
            )
        else:
            response = self._gateway_request(
                method="POST",
                path="/api/boolean-prompt",
                body=request,
                test=request.get("test", False),
                relay=True,
            )

        self._handle_signature(request, response)

        return response

    def text_prompt(self, request):
        # type: (dict) -> dict
        """Asks the consumer a text based question."""

        self._populate_signature_options(request)

        if self._is_terminal_routed(request.get("terminalName")):
            response = self._terminal_request(
                method="POST",
                path="/api/text-prompt",
                body=request,
                terminal=request.get("terminalName"),
            )
        else:
            response = self._gateway_request(
                method="POST",
                path="/api/text-prompt",
                body=request,
                test=request.get("test", False),
                relay=True,
            )

        self._handle_signature(request, response)

        return response


    def capture(self, request):
        # type: (dict) -> dict
        """Captures a preauthorization."""

        return self._gateway_request(
            method="POST",
            path="/api/capture",
            body=request,
            test=request.get("test", False),
        )

    def void(self, request):
        # type: (dict) -> dict
        """Discards a previous transaction."""

        return self._gateway_request(
            method="POST",
            path="/api/void",
            body=request,
            test=request.get("test", False),
        )

    def reverse(self, request):
        # type: (dict) -> dict
        """Executes a manual time out reversal.

        We love time out reversals. Don't be afraid to use them whenever a request to a
        BlockChyp terminal times out. You have up to two minutes to reverse any transaction.
        The only caveat is that you must assign transactionRef values when you build the
        original request. Otherwise, we have no real way of knowing which transaction
        you're trying to reverse because we may not have assigned it an id yet. And if we did
        assign it an id, you wouldn't know what it is because your request to the terminal
        timed out before you got a response.
        """

        return self._gateway_request(
            method="POST",
            path="/api/reverse",
            body=request,
            test=request.get("test", False),
        )

    def close_batch(self, request):
        # type: (dict) -> dict
        """Closes the current credit card batch."""

        return self._gateway_request(
            method="POST",
            path="/api/close-batch",
            body=request,
            test=request.get("test", False),
        )

    def send_payment_link(self, request):
        # type: (dict) -> dict
        """Creates and send a payment link to a customer."""

        return self._gateway_request(
            method="POST",
            path="/api/send-payment-link",
            body=request,
            test=request.get("test", False),
        )

    def transaction_status(self, request):
        # type: (dict) -> dict
        """Retrieves the current status of a transaction."""

        return self._gateway_request(
            method="POST",
            path="/api/tx-status",
            body=request,
            test=request.get("test", False),
        )

    def update_customer(self, request):
        # type: (dict) -> dict
        """Updates or creates a customer record."""

        return self._gateway_request(
            method="POST",
            path="/api/update-customer",
            body=request,
            test=request.get("test", False),
        )

    def customer(self, request):
        # type: (dict) -> dict
        """Retrieves a customer by id."""

        return self._gateway_request(
            method="POST",
            path="/api/customer",
            body=request,
            test=request.get("test", False),
        )

    def customer_search(self, request):
        # type: (dict) -> dict
        """Searches the customer database."""

        return self._gateway_request(
            method="POST",
            path="/api/customer-search",
            body=request,
            test=request.get("test", False),
        )

    def cash_discount(self, request):
        # type: (dict) -> dict
        """Calculates the discount for actual cash transactions."""

        return self._gateway_request(
            method="POST",
            path="/api/cash-discount",
            body=request,
            test=request.get("test", False),
        )

    def batch_history(self, request):
        # type: (dict) -> dict
        """Returns the batch history for a merchant."""

        return self._gateway_request(
            method="POST",
            path="/api/batch-history",
            body=request,
            test=request.get("test", False),
        )

    def batch_details(self, request):
        # type: (dict) -> dict
        """Returns the batch details for a single batch."""

        return self._gateway_request(
            method="POST",
            path="/api/batch-details",
            body=request,
            test=request.get("test", False),
        )

    def transaction_history(self, request):
        # type: (dict) -> dict
        """Returns the transaction history for a merchant."""

        return self._gateway_request(
            method="POST",
            path="/api/tx-history",
            body=request,
            test=request.get("test", False),
        )

    def merchant_profile(self, request):
        # type: (dict) -> dict
        """Returns profile information for a merchant."""

        return self._gateway_request(
            method="POST",
            path="/api/public-merchant-profile",
            body=request,
            test=request.get("test", False),
        )

    def _terminal_request(self, method, path, body, terminal, query=None):
        """Sends a request to a terminal."""
        route = self._resolve_terminal_route(terminal)
        url = self._assemble_terminal_url(route, path)

        credentials = route.get("transientCredentials", {
            "apiKey": self.api_key,
            "bearerToken": self.bearer_token,
            "signingKey": self.signing_key,
        })

        term_request = {
            "request": body,
            **credentials,
        }

        timeout = self._get_timeout(body, self.terminal_timeout)

        response = self.terminal_session.request(
            method,
            url,
            params=query,
            json=term_request,
            timeout=timeout,
        )

        return self._decode_response(response)

    def _assemble_terminal_url(self, route, path):
        # type: (dict, str) -> str
        if self.terminal_https:
            port = self.TERMINAL_HTTPS_PORT
            protocol = "https"
        else:
            port = self.TERMINAL_HTTP_PORT
            protocol = "http"

        return urllib.parse.urlunparse((
            protocol,
            f"{route.get('ipAddress')}:{port}",
            path, "", "", "",
        ))

    def _resolve_terminal_route(self, terminal):
        # type: (str) -> dict
        credentials = {
            "apiKey": self.api_key,
            "bearerToken": self.bearer_token,
            "signingKey": self.signing_key,
        }

        route = self.route_cache.get(terminal, credentials)
        if route:
            return route

        try:
            route = self._request_terminal_route(terminal)
            self.route_cache.put(route, {
                "apiKey": self.api_key,
                "signingKey": self.signing_key,
                "bearerToken": self.bearer_token,
            })
        except IOError:
            route = self.route_cache.get(terminal, credentials, include_expired=True)
            if not route:
                raise

        return route

    def _request_terminal_route(self, terminal):
        # type: (str) -> dict
        route = self._gateway_request(
            method="GET",
            path="/api/terminal-route",
            query={"terminal": terminal},
        )
        if route and route.get("success"):
            route["timestamp"] = iso_timestamp()

        return route

    def _is_terminal_routed(self, terminal):
        route = self._resolve_terminal_route(terminal)
        return route and route.get("success") and not route.get("cloudRelayEnabled")

    def _gateway_request(self, method, path, body=None, query=None, test=False, relay=False):
        """Sends a request to the gateway."""
        url = self._assemble_gateway_url(path, test)
        auth = crypto.auth_headers(self.api_key, self.bearer_token, self.signing_key)

        timeout = self._get_timeout(body, self.terminal_timeout if relay else self.gateway_timeout)

        response = self.internet_session.request(
            method,
            url,
            params=query,
            json=body,
            headers=auth,
            timeout=timeout,
        )

        return self._decode_response(response)

    def _assemble_gateway_url(self, path, test):
        # type: (str, bool) -> str
        base = self.gateway_url
        if test:
            base = self.gateway_test_url

        return urllib.parse.urljoin(base, path)

    def _build_session(self, adapter=None):
        session = requests.session()

        if adapter:
            session.mount("https://", adapter)

        session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": self.user_agent(),
        })

        return session

    @staticmethod
    def _get_timeout(request, default):
        try:
            return request.get("timeout", default)
        except AttributeError:
            return default

    @staticmethod
    def _populate_signature_options(request):
        if (
                not request.get("sigFile")
                or request.get("sigFormat", SignatureFormat.NONE) != SignatureFormat.NONE
        ):
            return

        fmt = request["sigFile"].split(os.extsep)[-1]
        if fmt not in (
                SignatureFormat.NONE,
                SignatureFormat.PNG,
                SignatureFormat.JPG,
                SignatureFormat.GIF
        ):
            raise ValueError("Invalid format: %s" % fmt)

        request["sigFormat"] = fmt

    @staticmethod
    def _handle_signature(request, response):
        if not request.get("sigFile") or not response.get("sigFile"):
            return

        raw = bytearray.fromhex(response.get("sigFile"))

        with io.open(request["sigFile"], "wb") as f:
            f.write(raw)

    @staticmethod
    def _decode_response(response):
        if not response.ok:
            raise BlockChypError(http_body=response.text, http_status=response.status_code)

        try:
            return response.json()
        except json.decoder.JSONDecodeError:
            raise BlockChypError("Malformed JSON", http_body=response.text)

    @classmethod
    def user_agent(cls):
        """API client user agent."""
        return f"BlockChyp-Python/{cls.version()}"

    @staticmethod
    def version():
        """Returns the version of the client."""
        return version.VERSION
