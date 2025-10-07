# Copyright 2019-2025 BlockChyp, Inc. All rights reserved. Use of this code is
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
def test_update_token():
    """Can update a token."""


    terminal = _get_test_config().get("defaultTerminalName")


    client = _get_test_client("")

    setup_request = {
        "pan": "4111111111111111",
        "test": True,
        "customer": {
            "customerRef": "TESTCUSTOMER",
            "firstName": "Test",
            "lastName": "Customer",
        },
    }

    setup_response = client.enroll(setup_request)
    print("Setup response: %r" % setup_response)

    assert setup_response.get("success")

    request = {
        "token": setup_response["token"],
        "expiryMonth": "12",
        "expiryYear": "2040",
    }

    response = client.update_token(request)
    print("Response: %r" % response)

    assert response.get("success") is True
