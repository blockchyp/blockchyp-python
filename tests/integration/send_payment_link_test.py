# Copyright 2019 BlockChyp, Inc. All rights reserved. Use of this code is
# governed by a license that can be found in the LICENSE file.
#
# This file was generated automatically. Changes to this file will be lost every
# time the code is regenerated.
import os
import time
import uuid

import pytest

import blockchyp

from .util import _get_test_client, _get_test_config


@pytest.mark.itest
def test_send_payment_link():
    """Can generate a payment link."""

    client = _get_test_client()
    terminal = _get_test_config().get("defaultTerminalName")

    delay = os.environ.get("BC_TEST_DELAY")
    if delay:
        client.message({
            "terminalName": terminal,
            "test": True,
            "message": f"Running send_payment_link in {delay}s",
        })
        time.sleep(int(delay))


    request = {
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
            "emailAddress": "support@blockchyp.com",
            "smsNumber": "(123) 123-1231",
        },
    }

    response = client.send_payment_link(request)

    print("Response: %r" % response)

    assert response.get("success") is True
    assert response.get("url")
