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
def test_empty_branding_asset():
    """Creates an empty terminal branding asset."""

    client = _get_test_client()
    terminal = _get_test_config().get("defaultTerminalName")

    delay = os.environ.get("BC_TEST_DELAY")
    if delay:
        client.message({
            "terminalName": terminal,
            "test": True,
            "message": f"Running empty_branding_asset in {delay}s",
        })
        time.sleep(int(delay))


    request = {
        "notes": "Empty Asset",
        "enabled": False,
    }

    response = client.update_branding_asset(request)

    print("Response: %r" % response)

    assert response.get("success") is True
