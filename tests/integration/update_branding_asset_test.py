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
def test_update_branding_asset():
    """Updates a terminal branding asset."""

    client = _get_test_client()
    terminal = _get_test_config().get("defaultTerminalName")

    delay = os.environ.get("BC_TEST_DELAY")
    if delay:
        client.message({
            "terminalName": terminal,
            "test": True,
            "message": f"Running update_branding_asset in {delay}s",
        })
        time.sleep(int(delay))


    setup_request = {
        "fileName": "aviato.png",
        "fileSize": 18843,
        "uploadId": str(uuid.uuid4()),
    }

    setup_response = client.upload_media(setup_request)

    print("Setup response: %r" % setup_response)

    assert setup_response.get("success")

    request = {
        "mediaId": ,
        "padded": True,
        "ordinal": 10,
        "startDate": "01/06/2021",
        "startTime": "14:00",
        "endDate": "11/05/2024",
        "endTime": "16:00",
        "notes": "Test Branding Asset",
        "preview": False,
        "enabled": True,
    }

    response = client.update_branding_asset(request)

    print("Response: %r" % response)

    assert response.get("success") is True
