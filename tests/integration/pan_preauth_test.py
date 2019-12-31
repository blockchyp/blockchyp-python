# Copyright 2019 BlockChyp, Inc. All rights reserved. Use of this code is
# governed by a license that can be found in the LICENSE file.
#
# This file was generated automatically. Changes to this file will be lost every
# time the code is regenerated.
import pytest

import blockchyp

from .util import _get_test_client


@pytest.mark.itest
def test_pan_preauth():
    """Can process a preauthorization by PAN."""

    client = _get_test_client()

    request = {
        "pan": "4111111111111111",
        "amount": "25.55",
        "test": True,
    }

    response = client.preauth(request)

    print("Response: %r" % response)

    assert response.get("approved") is True
    assert response.get("test") is True
    assert len(response.get("authCode")) == 6
    assert response.get("transactionId")
    assert response.get("timestamp")
    assert response.get("tickBlock")
    assert response.get("responseDescription") == "Approved"
    assert response.get("paymentType")
    assert response.get("maskedPan")
    assert response.get("entryMethod")
    assert response.get("authorizedAmount") == "25.55"
    assert response.get("entryMethod") == "KEYED"

