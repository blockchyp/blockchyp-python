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
def test_empty_slide_show():
    """Updates or creates an empty slide show."""


    terminal = _get_test_config().get("defaultTerminalName")


    client = _get_test_client("")

    request = {
        "name": "Test Slide Show",
        "delay": 5,
    }

    response = client.update_slide_show(request)
    print("Response: %r" % response)

    assert response.get("success") is True
    assert response.get("name") == "Test Slide Show"
