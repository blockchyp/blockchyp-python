# Copyright 2019-2023 BlockChyp, Inc. All rights reserved. Use of this code is
# governed by a license that can be found in the LICENSE file.
#
# This file was generated automatically by the BlockChyp SDK Generator. Changes
# to this file will be lost every time the code is regenerated.
import os
import os.path
import time
import uuid
import pkg_resources

import pytest

import blockchyp

from .util import _get_test_client, _get_test_config


@pytest.mark.itest
def test_payment_link_status():
    """Can return the status of a payment link."""


    terminal = _get_test_config().get("defaultTerminalName")


    client = _get_test_client("")

    setup_request = {
        "amount": "199.99",
        "description": "Widget",
        "subject": "Widget invoice",
        "transaction": {
            "subtotal": "195.00",
            "tax": "4.99",
            "total": "199.99",
            "items": [
                {
                    "description": "Widget",
                    "price": "195.00",
                    "quantity": 1,
                },
            ],
        },
        "autoSend": True,
        "customer": {
            "customerRef": "Customer reference string",
            "firstName": "FirstName",
            "lastName": "LastName",
            "companyName": "Company Name",
            "emailAddress": "notifications@blockchypteam.m8r.co",
            "smsNumber": "(123) 123-1231",
        },
    }

    setup_response = client.send_payment_link(setup_request)
    print("Setup response: %r" % setup_response)

    assert setup_response.get("success")

    request = {
        "linkCode": setup_response["linkCode"],
    }

    response = client.payment_link_status(request)
    print("Response: %r" % response)

    assert response.get("success") is True
