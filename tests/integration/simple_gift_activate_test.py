# Copyright 2019 BlockChyp, Inc. All rights reserved. Use of this code is
# governed by a license that can be found in the LICENSE file.
#
# This file was generated automatically. Changes to this file will be lost every
# time the code is regenerated.
import pytest

import blockchyp

from .util import _get_test_client


@pytest.mark.itest
def test_simple_gift_activate():
    """Can activate a blockchain gift card."""

    client = _get_test_client()

    request = {
        "test": True,
        "terminalName": "Test Terminal",
        "amount": "50.00",
    }

    response = client.gift_activate(request)

    print("Response: %r" % response)

    assert response.get("approved") is True
    assert response.get("publicKey")

