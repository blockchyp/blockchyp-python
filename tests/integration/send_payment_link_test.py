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
def test_send_payment_link():
    """Can generate a payment link."""


    terminal = _get_test_config().get("defaultTerminalName")


    client = _get_test_client("")

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
            "emailAddress": "notifications@blockchypteam.m8r.co",
            "smsNumber": "(123) 123-1231",
        },
    }

    response = client.send_payment_link(request)
    print("Response: %r" % response)

    assert response.get("success") is True
    assert response.get("url")
