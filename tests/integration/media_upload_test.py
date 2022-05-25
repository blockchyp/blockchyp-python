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
def test_media_upload():
    """MediaUpload."""

    client = _get_test_client()
    terminal = _get_test_config().get("defaultTerminalName")

    delay = os.environ.get("BC_TEST_DELAY")
    if delay:
        client.message({
            "terminalName": terminal,
            "test": True,
            "message": f"Running media_upload in {delay}s",
        })
        time.sleep(int(delay))


    request = {
        "fileName": "aviato.png",
        "fileSize": 18843,
        "uploadId": str(uuid.uuid4()),
    }

    response = client.upload_media(request)

    print("Response: %r" % response)

    assert response.get("success") is True
    assert response.get("id")
    assert response.get("originalFile") == "aviato.png"
    assert response.get("fileUrl")
    assert response.get("thumbnailUrl")
