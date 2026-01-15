# Copyright 2019-2026 BlockChyp, Inc. All rights reserved. Use of this code is
# governed by a license that can be found in the LICENSE file.
#
# This file was generated automatically by the BlockChyp SDK Generator. Changes
# to this file will be lost every time the code is regenerated.
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

from typing import Any

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
        self.dashboard_url = "https://dashboard.blockchyp.com"

        self.gateway_timeout = 20 # Seconds

        # Default terminal configuration
        self.terminal_https = True

        self.terminal_timeout = 60 * 2 # Seconds

        self.internet_session = self._build_session()
        self.upload_session = self._build_upload_session()
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

    def card_metadata(self, request):
        # type: (dict) -> dict
        """Retrieves card metadata."""

        self._populate_signature_options(request)

        if self._is_terminal_routed(request.get("terminalName")):
            response = self._terminal_request(
                method="POST",
                path="/api/card-metadata",
                body=request,
                terminal=request.get("terminalName"),
            )
        else:
            response = self._gateway_request(
                method="POST",
                path="/api/card-metadata",
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

    def list_queued_transactions(self, request):
        # type: (dict) -> dict
        """Returns a list of queued transactions on a terminal."""

        self._populate_signature_options(request)

        if self._is_terminal_routed(request.get("terminalName")):
            response = self._terminal_request(
                method="POST",
                path="/api/queue/list",
                body=request,
                terminal=request.get("terminalName"),
            )
        else:
            response = self._gateway_request(
                method="POST",
                path="/api/queue/list",
                body=request,
                test=request.get("test", False),
                relay=True,
            )

        self._handle_signature(request, response)

        return response

    def delete_queued_transaction(self, request):
        # type: (dict) -> dict
        """Deletes a queued transaction from the terminal."""

        self._populate_signature_options(request)

        if self._is_terminal_routed(request.get("terminalName")):
            response = self._terminal_request(
                method="POST",
                path="/api/queue/delete",
                body=request,
                terminal=request.get("terminalName"),
            )
        else:
            response = self._gateway_request(
                method="POST",
                path="/api/queue/delete",
                body=request,
                test=request.get("test", False),
                relay=True,
            )

        self._handle_signature(request, response)

        return response

    def reboot(self, request):
        # type: (dict) -> dict
        """Reboot a payment terminal."""

        self._populate_signature_options(request)

        if self._is_terminal_routed(request.get("terminalName")):
            response = self._terminal_request(
                method="POST",
                path="/api/reboot",
                body=request,
                terminal=request.get("terminalName"),
            )
        else:
            response = self._gateway_request(
                method="POST",
                path="/api/terminal-reboot",
                body=request,
                test=request.get("test", False),
                relay=True,
            )

        self._handle_signature(request, response)

        return response


    def locate(self, request):
        # type: (dict) -> dict
        """Returns routing and location data for a payment terminal."""

        return self._gateway_request(
            method="POST",
            path="/api/terminal-locate",
            body=request,
            test=request.get("test", False),
        )

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

    def resend_payment_link(self, request):
        # type: (dict) -> dict
        """Resends payment link."""

        return self._gateway_request(
            method="POST",
            path="/api/resend-payment-link",
            body=request,
            test=request.get("test", False),
        )

    def cancel_payment_link(self, request):
        # type: (dict) -> dict
        """Cancels a payment link."""

        return self._gateway_request(
            method="POST",
            path="/api/cancel-payment-link",
            body=request,
            test=request.get("test", False),
        )

    def payment_link_status(self, request):
        # type: (dict) -> dict
        """Retrieves the status of a payment link."""

        return self._gateway_request(
            method="POST",
            path="/api/payment-link-status",
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

    def pricing_policy(self, request):
        # type: (dict) -> dict
        """Returns pricing policy for a merchant."""

        return self._gateway_request(
            method="POST",
            path="/api/read-pricing-policy",
            body=request,
            test=request.get("test", False),
        )

    def partner_statements(self, request):
        # type: (dict) -> dict
        """Returns a list of partner statements."""

        return self._gateway_request(
            method="POST",
            path="/api/partner-statement-list",
            body=request,
            test=request.get("test", False),
        )

    def partner_statement_detail(self, request):
        # type: (dict) -> dict
        """Returns detail for a single partner statement."""

        return self._gateway_request(
            method="POST",
            path="/api/partner-statement-detail",
            body=request,
            test=request.get("test", False),
        )

    def merchant_invoices(self, request):
        # type: (dict) -> dict
        """Returns a list of merchant invoices."""

        return self._gateway_request(
            method="POST",
            path="/api/merchant-invoice-list",
            body=request,
            test=request.get("test", False),
        )

    def merchant_invoice_detail(self, request):
        # type: (dict) -> dict
        """Returns detail for a single merchant-invoice statement."""

        return self._gateway_request(
            method="POST",
            path="/api/merchant-invoice-detail",
            body=request,
            test=request.get("test", False),
        )

    def partner_commission_breakdown(self, request):
        # type: (dict) -> dict
        """Returns low level details for how partner commissions were calculated for a
        specific merchant statement.
        """

        return self._gateway_request(
            method="POST",
            path="/api/partner-commission-breakdown",
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

    def delete_customer(self, request):
        # type: (dict) -> dict
        """Deletes a customer record."""

        return self._gateway_request(
            method="DELETE",
            path="/api/customer/" + request["customerId"],
            body=request,
            test=request.get("test", False),
        )

    def token_metadata(self, request):
        # type: (dict) -> dict
        """Retrieves payment token metadata."""

        return self._gateway_request(
            method="GET",
            path="/api/token/" + request["token"],
            body=request,
            test=request.get("test", False),
        )

    def link_token(self, request):
        # type: (dict) -> dict
        """Links a token to a customer record."""

        return self._gateway_request(
            method="POST",
            path="/api/link-token",
            body=request,
            test=request.get("test", False),
        )

    def unlink_token(self, request):
        # type: (dict) -> dict
        """Removes a link between a customer and a token."""

        return self._gateway_request(
            method="POST",
            path="/api/unlink-token",
            body=request,
            test=request.get("test", False),
        )

    def update_token(self, request):
        # type: (dict) -> dict
        """Updates a payment token."""

        return self._gateway_request(
            method="POST",
            path="/api/token/" + request["token"],
            body=request,
            test=request.get("test", False),
        )

    def delete_token(self, request):
        # type: (dict) -> dict
        """Deletes a payment token."""

        return self._gateway_request(
            method="DELETE",
            path="/api/token/" + request["token"],
            body=request,
            test=request.get("test", False),
        )


    def merchant_credential_generation(self, request):
        # type: (dict) -> dict
        """Generates and returns api credentials for a given merchant."""

        return self._dashboard_request(
            method="POST",
            path="/api/generate-merchant-creds",
            body=request,
        )

    def submit_application(self, request):
        # type: (dict) -> dict
        """Submits and application to add a new merchant account."""

        return self._dashboard_request(
            method="POST",
            path="/api/submit-application",
            body=request,
        )

    def get_merchants(self, request):
        # type: (dict) -> dict
        """Adds a test merchant account."""

        return self._dashboard_request(
            method="POST",
            path="/api/get-merchants",
            body=request,
        )

    def update_merchant(self, request):
        # type: (dict) -> dict
        """Adds or updates a merchant account. Can be used to create or update test
        merchants. Only gateway partners may create new live merchants.
        """

        return self._dashboard_request(
            method="POST",
            path="/api/update-merchant",
            body=request,
        )

    def merchant_users(self, request):
        # type: (dict) -> dict
        """List all active users and pending invites for a merchant account."""

        return self._dashboard_request(
            method="POST",
            path="/api/merchant-users",
            body=request,
        )

    def invite_merchant_user(self, request):
        # type: (dict) -> dict
        """Invites a user to join a merchant account."""

        return self._dashboard_request(
            method="POST",
            path="/api/invite-merchant-user",
            body=request,
        )

    def add_gateway_merchant(self, request):
        # type: (dict) -> dict
        """Adds a live gateway merchant account."""

        return self._dashboard_request(
            method="POST",
            path="/api/add-gateway-merchant",
            body=request,
        )

    def add_test_merchant(self, request):
        # type: (dict) -> dict
        """Adds a test merchant account."""

        return self._dashboard_request(
            method="POST",
            path="/api/add-test-merchant",
            body=request,
        )

    def delete_test_merchant(self, request):
        # type: (dict) -> dict
        """Deletes a test merchant account. Supports partner scoped API credentials only.
        Live merchant accounts cannot be deleted.
        """

        return self._dashboard_request(
            method="DELETE",
            path="/api/test-merchant/" + request["merchantId"],
            body=request,
        )

    def merchant_platforms(self, request):
        # type: (dict) -> dict
        """List all merchant platforms configured for a gateway merchant."""

        return self._dashboard_request(
            method="GET",
            path="/api/plugin-configs/" + request["merchantId"],
            body=request,
        )

    def update_merchant_platforms(self, request):
        # type: (dict) -> dict
        """List all merchant platforms configured for a gateway merchant."""

        return self._dashboard_request(
            method="POST",
            path="/api/plugin-configs",
            body=request,
        )

    def delete_merchant_platforms(self, request):
        # type: (dict) -> dict
        """Deletes a boarding platform configuration."""

        return self._dashboard_request(
            method="DELETE",
            path="/api/plugin-config/" + request["platformId"],
            body=request,
        )

    def terminals(self, request):
        # type: (dict) -> dict
        """Returns all terminals associated with the merchant account."""

        return self._dashboard_request(
            method="GET",
            path="/api/terminals",
            body=request,
        )

    def deactivate_terminal(self, request):
        # type: (dict) -> dict
        """Deactivates a terminal."""

        return self._dashboard_request(
            method="DELETE",
            path="/api/terminal/" + request["terminalId"],
            body=request,
        )

    def activate_terminal(self, request):
        # type: (dict) -> dict
        """Activates a terminal."""

        return self._dashboard_request(
            method="POST",
            path="/api/terminal-activate",
            body=request,
        )

    def tc_templates(self, request):
        # type: (dict) -> dict
        """Returns a list of terms and conditions templates associated with a merchant
        account.
        """

        return self._dashboard_request(
            method="GET",
            path="/api/tc-templates",
            body=request,
        )

    def tc_template(self, request):
        # type: (dict) -> dict
        """Returns a single terms and conditions template."""

        return self._dashboard_request(
            method="GET",
            path="/api/tc-templates/" + request["templateId"],
            body=request,
        )

    def tc_update_template(self, request):
        # type: (dict) -> dict
        """Updates or creates a terms and conditions template."""

        return self._dashboard_request(
            method="POST",
            path="/api/tc-templates",
            body=request,
        )

    def tc_delete_template(self, request):
        # type: (dict) -> dict
        """Deletes a single terms and conditions template."""

        return self._dashboard_request(
            method="DELETE",
            path="/api/tc-templates/" + request["templateId"],
            body=request,
        )

    def tc_log(self, request):
        # type: (dict) -> dict
        """Returns up to 250 entries from the Terms and Conditions log."""

        return self._dashboard_request(
            method="POST",
            path="/api/tc-log",
            body=request,
        )

    def tc_entry(self, request):
        # type: (dict) -> dict
        """Returns a single detailed Terms and Conditions entry."""

        return self._dashboard_request(
            method="GET",
            path="/api/tc-entry/" + request["logEntryId"],
            body=request,
        )

    def survey_questions(self, request):
        # type: (dict) -> dict
        """Returns all survey questions for a given merchant."""

        return self._dashboard_request(
            method="GET",
            path="/api/survey-questions",
            body=request,
        )

    def survey_question(self, request):
        # type: (dict) -> dict
        """Returns a single survey question with response data."""

        return self._dashboard_request(
            method="GET",
            path="/api/survey-questions/" + request["questionId"],
            body=request,
        )

    def update_survey_question(self, request):
        # type: (dict) -> dict
        """Updates or creates a survey question."""

        return self._dashboard_request(
            method="POST",
            path="/api/survey-questions",
            body=request,
        )

    def delete_survey_question(self, request):
        # type: (dict) -> dict
        """Deletes a survey question."""

        return self._dashboard_request(
            method="DELETE",
            path="/api/survey-questions/" + request["questionId"],
            body=request,
        )

    def survey_results(self, request):
        # type: (dict) -> dict
        """Returns results for a single survey question."""

        return self._dashboard_request(
            method="POST",
            path="/api/survey-results",
            body=request,
        )

    def media(self, request):
        # type: (dict) -> dict
        """Returns the media library for a given partner, merchant, or organization."""

        return self._dashboard_request(
            method="GET",
            path="/api/media",
            body=request,
        )

    def upload_media(self, request, content):
        # type: (dict, Any) -> dict
        """Uploads a media asset to the media library."""

        return self._upload_request(
            path="/api/upload-media",
            request=request,
            content=content,
        )


    def upload_status(self, request):
        # type: (dict) -> dict
        """Retrieves the current status of a file upload."""

        return self._dashboard_request(
            method="GET",
            path="/api/media-upload/" + request["uploadId"],
            body=request,
        )

    def media_asset(self, request):
        # type: (dict) -> dict
        """Returns the media details for a single media asset."""

        return self._dashboard_request(
            method="GET",
            path="/api/media/" + request["mediaId"],
            body=request,
        )

    def delete_media_asset(self, request):
        # type: (dict) -> dict
        """Deletes a media asset."""

        return self._dashboard_request(
            method="DELETE",
            path="/api/media/" + request["mediaId"],
            body=request,
        )

    def slide_shows(self, request):
        # type: (dict) -> dict
        """Returns a collection of slide shows."""

        return self._dashboard_request(
            method="GET",
            path="/api/slide-shows",
            body=request,
        )

    def slide_show(self, request):
        # type: (dict) -> dict
        """Returns a single slide show with slides."""

        return self._dashboard_request(
            method="GET",
            path="/api/slide-shows/" + request["slideShowId"],
            body=request,
        )

    def update_slide_show(self, request):
        # type: (dict) -> dict
        """Updates or creates a slide show."""

        return self._dashboard_request(
            method="POST",
            path="/api/slide-shows",
            body=request,
        )

    def delete_slide_show(self, request):
        # type: (dict) -> dict
        """Deletes a single slide show."""

        return self._dashboard_request(
            method="DELETE",
            path="/api/slide-shows/" + request["slideShowId"],
            body=request,
        )

    def terminal_branding(self, request):
        # type: (dict) -> dict
        """Returns the terminal branding stack for a given set of API credentials."""

        return self._dashboard_request(
            method="GET",
            path="/api/terminal-branding",
            body=request,
        )

    def update_branding_asset(self, request):
        # type: (dict) -> dict
        """Updates a branding asset."""

        return self._dashboard_request(
            method="POST",
            path="/api/terminal-branding",
            body=request,
        )

    def delete_branding_asset(self, request):
        # type: (dict) -> dict
        """Deletes a branding asset."""

        return self._dashboard_request(
            method="DELETE",
            path="/api/terminal-branding/" + request["assetId"],
            body=request,
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

    def _upload_request(self, path, request, content, query=None):
        """Sends a request to the dashboard."""
        url = self._assemble_dashboard_url(path)
        auth = crypto.auth_headers(self.api_key, self.bearer_token, self.signing_key)

        if request["fileName"]:
            auth["X-Upload-File-Name"] = request["fileName"]

        if request["uploadId"]:
            auth["X-Upload-ID"] = request["uploadId"]

        if request["fileSize"]:
            auth["X-File-Size"] = str(request["fileSize"])
            auth["Content-Length"] = str(request["fileSize"])


        timeout = self._get_timeout(request, self.gateway_timeout)

        response = self.upload_session.request(
            "POST",
            url,
            params=query,
            data=content,
            headers=auth,
            timeout=timeout,
        )

        return self._decode_response(response)


    def _dashboard_request(self, method, path, body=None, query=None):
        """Sends a request to the dashboard."""
        url = self._assemble_dashboard_url(path)
        auth = crypto.auth_headers(self.api_key, self.bearer_token, self.signing_key)

        timeout = self._get_timeout(body, self.gateway_timeout)

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

    def _assemble_dashboard_url(self, path):
        # type: (str) -> str
        base = self.dashboard_url
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

    def _build_upload_session(self, adapter=None):
        session = requests.session()

        if adapter:
            session.mount("https://", adapter)

        session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/octet-stream",
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
