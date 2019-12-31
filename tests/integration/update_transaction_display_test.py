# Copyright 2019 BlockChyp, Inc. All rights reserved. Use of this code is
# governed by a license that can be found in the LICENSE file.
#
# This file was generated automatically. Changes to this file will be lost every
# time the code is regenerated.
import pytest

import blockchyp

from .util import _get_test_client


@pytest.mark.itest
def test_update_transaction_display():
    """Can update transaction line item display."""

    client = _get_test_client()

    request = {
        "test": True,
        "terminalName": "Test Terminal",
        "transaction": {
            "subtotal": "35.00",
            "tax": "5.00",
            "total": "70.00",
            "items": [
                {
                    "description": "Leki Trekking Poles",
                    "price": "35.00",
                    "quantity": 2,
                    "extended": "70.00",
                    "discounts": [
                        {
                            "description": "memberDiscount",
                            "amount": "10.00",
                        },
                    ],
                },
            ],
        },
    }

    response = client.update_transaction_display(request)

    print("Response: %r" % response)

    assert response.get("success") is True

