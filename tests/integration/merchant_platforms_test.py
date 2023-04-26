# Copyright 2019-2022 BlockChyp, Inc. All rights reserved. Use of this code is
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
def test_merchant_platforms():
    """Returns all platforms configured for a gateway only merchant."""


    terminal = _get_test_config().get("defaultTerminalName")


    client = _get_test_client("partner")

    setup_request = {
        "dbaName": "Test Merchant",
        "companyName": "Test Merchant",
    }

    setup_response = client.add_test_merchant(setup_request)
    print("Setup response: %r" % setup_response)

    assert setup_response.get("success")

    request = {
        "merchantId": setup_response["merchantId"],
    }

    response = client.merchant_platforms(request)
    print("Response: %r" % response)

    assert response.get("success") is True
