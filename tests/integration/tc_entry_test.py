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
def test_tc_entry():
    """Returns a detailed terms and conditions entry."""

    client = _get_test_client()
    terminal = _get_test_config().get("defaultTerminalName")

    delay = os.environ.get("BC_TEST_DELAY")
    if delay:
        client.message({
            "terminalName": terminal,
            "test": True,
            "message": f"Running tc_entry in {delay}s",
        })
        time.sleep(int(delay))


    setup_request = {
    }

    setup_response = client.tc_log(setup_request)

    print("Setup response: %r" % setup_response)

    assert setup_response.get("success")

    request = {
        "logEntryId": ,
    }

    response = client.tc_entry(request)

    print("Response: %r" % response)

    assert response.get("success") is True
    assert response.get("id")
    assert response.get("terminalId")
    assert response.get("terminalName")
    assert response.get("timestamp")
    assert response.get("name")
    assert response.get("content")
    assert response.get("hasSignature") is True
    assert response.get("signature")
