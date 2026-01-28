# Copyright 2019-2026 BlockChyp, Inc. All rights reserved. Use of this code is
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
def test_update_merchant():
    """Updates or creates a merchant account."""


    terminal = _get_test_config().get("defaultTerminalName")


    client = _get_test_client("partner")

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
