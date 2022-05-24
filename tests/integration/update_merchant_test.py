# Copyright 2019-2022 BlockChyp, Inc. All rights reserved. Use of this code is
# governed by a license that can be found in the LICENSE file.
#
# This file was generated automatically by the BlockChyp SDK Generator. Changes
# to this file will be lost every time the code is regenerated.
import os
import time
import uuid

import pytest

import blockchyp

from .util import _get_test_client, _get_test_config


@pytest.mark.itest
def test_update_merchant():
    """Updates or creates a merchant account."""

    client = _get_test_client()
    terminal = _get_test_config().get("defaultTerminalName")

    delay = os.environ.get("BC_TEST_DELAY")
    if delay:
        client.message({
            "terminalName": terminal,
            "test": True,
            "message": f"Running update_merchant in {delay}s",
        })
        time.sleep(int(delay))


    request = {
        "test": True,
        "dbaName": "Test Merchant",
        "companyName": "Test Merchant",
        "billingAddress": {
            "address1": "1060 West Addison",
            "city": "Chicago",
            "stateOrProvince": "IL",
            "postalCode": "60613",
        },
    }

    response = client.update_merchant(request)

    print("Response: %r" % response)

    assert response.get("success") is True
