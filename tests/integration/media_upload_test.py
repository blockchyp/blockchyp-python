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
def test_media_upload():
    """MediaUpload."""


    terminal = _get_test_config().get("defaultTerminalName")


    client = _get_test_client("")

    request = {
        "fileName": "aviato.png",
        "fileSize": 18843,
        "uploadId": str(uuid.uuid4()),
    }

    file_name = pkg_resources.resource_filename("tests", "resources/aviato.png")
    f = open(file_name, "rb")
    content = f.read()
    response = client.upload_media(request, content)
    f.close()
    print("Response: %r" % response)

    assert response.get("success") is True
    assert response.get("id")
    assert response.get("originalFile") == "aviato.png"
    assert response.get("fileUrl")
    assert response.get("thumbnailUrl")
