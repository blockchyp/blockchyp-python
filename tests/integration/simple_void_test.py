# Copyright 2019 BlockChyp, Inc. All rights reserved. Use of this code is
# governed by a license that can be found in the LICENSE file.
#
# This file was generated automatically. Changes to this file will be lost every
# time the code is regenerated.
import pytest

import blockchyp

from .util import _get_test_client


@pytest.mark.itest
def test_simple_void():
    """Can void a tranaction in the current batch."""

    client = _get_test_client()

    setup_request = {
        "pan": "4111111111111111",
        "amount": "25.55",
        "test": True,
        "transactionRef": ,
    }

    setup_response = client.charge(setup_request)

    print("Setup response: %r" % setup_response)

    assert setup_response.get("approved")

    request = {
        "transactionId": setup_response["transactionId"],
        "test": True,
    }

    response = client.void(request)

    print("Response: %r" % response)

    assert response.get("approved") is True

