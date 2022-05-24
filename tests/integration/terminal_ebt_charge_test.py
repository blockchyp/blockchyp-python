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
def test_terminal_ebt_charge():
    """Can process an ebt direct charge with a terminal."""

    client = _get_test_client()
    terminal = _get_test_config().get("defaultTerminalName")

    delay = os.environ.get("BC_TEST_DELAY")
    if delay:
        client.message({
            "terminalName": terminal,
            "test": True,
            "message": f"Running terminal_ebt_charge in {delay}s",
        })
        time.sleep(int(delay))


    request = {
        "terminalName": terminal,
        "amount": "25.00",
        "test": True,
        "cardType": blockchyp.CardType.EBT,
    }

    response = client.charge(request)

    print("Response: %r" % response)

    assert response.get("success") is True
    assert response.get("approved") is True
    assert response.get("test") is True
    assert len(response.get("authCode")) == 6
    assert response.get("transactionId")
    assert response.get("timestamp")
    assert response.get("tickBlock")
    assert response.get("responseDescription") == "approved"
    assert response.get("paymentType")
    assert response.get("maskedPan")
    assert response.get("entryMethod")
    assert response.get("authorizedAmount") == "25.00"
    assert response.get("remainingBalance") == "75.00"
