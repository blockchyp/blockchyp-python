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
def test_get_customer():
    """Can get a customer."""

    client = _get_test_client()

    delay = os.environ.get("BC_TEST_DELAY")
    if delay:
        client.message({
            "terminalName": _get_test_config().get("defaultTerminalName"),
            "test": True,
            "message": f"Running get_customer in {delay}s",
        })
        time.sleep(int(delay))


    setup_request = {
        "customer": {
            "firstName": "Test",
            "lastName": "Customer",
            "companyName": "Test Company",
            "emailAddress": "support@blockchyp.com",
            "smsNumber": "(123) 123-1234",
        },
    }

    setup_response = client.update_customer(setup_request)

    print("Setup response: %r" % setup_response)

    assert setup_response.get("success")

    request = {
        "customerId": setup_response.get("customer", {}).get("id"),
    }

    response = client.customer(request)

    print("Response: %r" % response)

    assert response.get("success") is True
