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
def test_terminal_gift_card_balance():
    """Can check the balance of an gift card card."""

    client = _get_test_client()

    delay = os.environ.get("BC_TEST_DELAY")
    if delay:
        client.message({
            "terminalName": _get_test_config().get("defaultTerminalName"),
            "test": True,
            "message": f"Running terminal_gift_card_balance in {delay}s",
        })
        time.sleep(int(delay))


    request = {
        "test": True,
        "terminalName": "Test Terminal",
    }

    response = client.balance(request)

    print("Response: %r" % response)

    assert response.get("success") is True
    assert response.get("remainingBalance")

