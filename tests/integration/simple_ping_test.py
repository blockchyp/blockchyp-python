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
def test_simple_ping():
    """Can test communication with a terminal."""


    terminal = _get_test_config().get("defaultTerminalName")

    client = _get_test_client("")
    delay = os.environ.get("BC_TEST_DELAY")
    if delay:
        client.message({
            "terminalName": terminal,
            "test": True,
            "message": f"Running simple_ping in {delay}s",
        })
        time.sleep(int(delay))

    client = _get_test_client("")

    request = {
        "test": True,
        "terminalName": terminal,
    }

    response = client.ping(request)
    print("Response: %r" % response)

    assert response.get("success") is True
