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
def test_add_test_merchant():
    """Can add a test merchant."""


    terminal = _get_test_config().get("defaultTerminalName")


    client = _get_test_client("partner")

    request = {
        "dbaName": "Test Merchant",
        "companyName": "Test Merchant",
    }

    response = client.add_test_merchant(request)
    print("Response: %r" % response)

    assert response.get("success") is True
    assert response.get("dbaName") == "Test Merchant"
    assert response.get("companyName") == "Test Merchant"
    assert response.get("visa") is True
