# Copyright 2019-2022 BlockChyp, Inc. All rights reserved. Use of this code is
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
def test_activate_terminal():
    """Activates a terminal."""


    terminal = _get_test_config().get("defaultTerminalName")


    client = _get_test_client("")

    request = {
        "terminalName": "Bad Terminal Code",
        "activationCode": "XXXXXX",
    }

    response = client.activate_terminal(request)
    print("Response: %r" % response)

    assert response.get("success") is False
    assert response.get("error") == "Invalid Activation Code"
