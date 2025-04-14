# Copyright 2019-2025 BlockChyp, Inc. All rights reserved. Use of this code is
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
def test_delete_queued_transaction():
    """Deletes a queued transaction the terminal."""


    terminal = _get_test_config().get("defaultTerminalName")

    client = _get_test_client("")
    delay = os.environ.get("BC_TEST_DELAY")
    if delay:
        client.message({
            "terminalName": terminal,
            "test": True,
            "message": f"Running delete_queued_transaction in {delay}s",
        })
        time.sleep(int(delay))

    client = _get_test_client("")

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
        "transactionRef": "*",
    }

    response = client.delete_queued_transaction(request)
    print("Response: %r" % response)

    assert response.get("success") is True
