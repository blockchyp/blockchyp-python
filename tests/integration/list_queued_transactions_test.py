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
def test_list_queued_transactions():
    """Lists queued transactions on terminal."""

    client = _get_test_client()
    terminal = _get_test_config().get("defaultTerminalName")

    delay = os.environ.get("BC_TEST_DELAY")
    if delay:
        client.message({
            "terminalName": terminal,
            "test": True,
            "message": f"Running list_queued_transactions in {delay}s",
        })
        time.sleep(int(delay))


    setup_request = {
        "terminalName": terminal,
        "transactionRef": str(uuid.uuid4()),
        "description": "1060 West Addison",
        "amount": "25.15",
        "test": True,
        "queue": True,
    }

    setup_response = client.charge(setup_request)

    print("Setup response: %r" % setup_response)

    assert setup_response.get("success")

    request = {
        "terminalName": terminal,
    }

    response = client.list_queued_transactions(request)

    print("Response: %r" % response)

    assert response.get("success") is True