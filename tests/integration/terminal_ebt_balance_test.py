# Copyright 2019 BlockChyp, Inc. All rights reserved. Use of this code is
# governed by a license that can be found in the LICENSE file.
#
# This file was generated automatically. Changes to this file will be lost every
# time the code is regenerated.
import pytest

import blockchyp

from .util import _get_test_client


@pytest.mark.itest
def test_terminal_ebt_balance():
    """Can check the balance of an EBT card."""

    client = _get_test_client()

    request = {
        "test": True,
        "terminalName": "Test Terminal",
        "cardType": blockchyp.CardType.EBT,
    }

    response = client.balance(request)

    print("Response: %r" % response)

    assert response.get("success") is True
    assert response.get("remainingBalance")

