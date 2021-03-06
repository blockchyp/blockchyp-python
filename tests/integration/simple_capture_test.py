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
def test_simple_capture():
    """Can capture a preauthorization."""

    client = _get_test_client()

    delay = os.environ.get("BC_TEST_DELAY")
    if delay:
        client.message({
            "terminalName": _get_test_config().get("defaultTerminalName"),
            "test": True,
            "message": f"Running simple_capture in {delay}s",
        })
        time.sleep(int(delay))


    setup_request = {
        "pan": "4111111111111111",
        "expMonth": "12",
        "expYear": "2025",
        "amount": "25.55",
        "test": True,
    }

    setup_response = client.preauth(setup_request)

    print("Setup response: %r" % setup_response)

    assert setup_response.get("success")

    request = {
        "transactionId": setup_response["transactionId"],
        "test": True,
    }

    response = client.capture(request)

    print("Response: %r" % response)

    assert response.get("success") is True
    assert response.get("approved") is True
