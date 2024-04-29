# Copyright 2019-2024 BlockChyp, Inc. All rights reserved. Use of this code is
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
def test_simple_reversal():
    """Can execute a time out reversal."""


    terminal = _get_test_config().get("defaultTerminalName")


    client = _get_test_client("")

    setup_request = {
        "pan": "4111111111111111",
        "expMonth": "12",
        "expYear": "2025",
        "amount": "25.55",
        "test": True,
        "transactionRef": str(uuid.uuid4()),
    }

    setup_response = client.charge(setup_request)
    print("Setup response: %r" % setup_response)

    assert setup_response.get("success")

    request = {
        "transactionRef": setup_response["transactionRef"],
        "test": True,
    }

    response = client.reverse(request)
    print("Response: %r" % response)

    assert response.get("success") is True
    assert response.get("approved") is True
