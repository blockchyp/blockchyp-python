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
def test_update_customer():
    """Can update a customer."""


    terminal = _get_test_config().get("defaultTerminalName")


    client = _get_test_client("")

    request = {
        "customer": {
            "firstName": "Test",
            "lastName": "Customer",
            "companyName": "Test Company",
            "emailAddress": "support@blockchyp.com",
            "smsNumber": "(123) 123-1234",
        },
    }

    response = client.update_customer(request)
    print("Response: %r" % response)

    assert response.get("success") is True
