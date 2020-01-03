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
def test_simple_reversal():
    """Can execute a time out reversal."""

    client = _get_test_client()

    delay = os.environ.get("BC_TEST_DELAY")
    if delay:
        client.message({
            "terminalName": _get_test_config().get("defaultTerminalName"),
            "test": True,
            "message": f"Running simple_reversal in {delay}s",
        })
        time.sleep(int(delay))


    setup_request = {
        "pan": "4111111111111111",
        "amount": "25.55",
        "test": True,
        "transactionRef": str(uuid.uuid4()),
    }

    setup_response = client.charge(setup_request)

    print("Setup response: %r" % setup_response)

    assert setup_response.get("approved")

    request = {
        "transactionRef": setup_response["transactionRef"],
        "test": True,
    }

    response = client.reverse(request)

    print("Response: %r" % response)

    assert response.get("approved") is True

