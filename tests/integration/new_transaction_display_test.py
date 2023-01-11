# Copyright 2019-2023 BlockChyp, Inc. All rights reserved. Use of this code is
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
def test_new_transaction_display():
    """Can reset transaction line item display."""


    terminal = _get_test_config().get("defaultTerminalName")

    client = _get_test_client("")
    delay = os.environ.get("BC_TEST_DELAY")
    if delay:
        client.message({
            "terminalName": terminal,
            "test": True,
            "message": f"Running new_transaction_display in {delay}s",
        })
        time.sleep(int(delay))

    client = _get_test_client("")

    request = {
        "test": True,
        "terminalName": terminal,
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

    response = client.new_transaction_display(request)
    print("Response: %r" % response)

    assert response.get("success") is True
