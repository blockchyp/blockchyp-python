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
def test_gateway_timeout():
    """Can specify gateway request timeouts."""

    client = _get_test_client()
    terminal = _get_test_config().get("defaultTerminalName")

    delay = os.environ.get("BC_TEST_DELAY")
    if delay:
        client.message({
            "terminalName": terminal,
            "test": True,
            "message": f"Running gateway_timeout in {delay}s",
        })
        time.sleep(int(delay))


    request = {
        "timeout": 1,
        "pan": "5555555555554444",
        "expMonth": "12",
        "expYear": "2025",
        "amount": "25.55",
        "test": True,
        "transactionRef": str(uuid.uuid4()),
    }

    with pytest.raises(IOError):
        client.charge(request)
