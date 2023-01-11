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
def test_update_branding_asset():
    """Updates a terminal branding asset."""


    terminal = _get_test_config().get("defaultTerminalName")


    client = _get_test_client("")

    setup_request = {
        "fileName": "aviato.png",
        "fileSize": 18843,
        "uploadId": str(uuid.uuid4()),
    }

    file_name = pkg_resources.resource_filename("tests", "resources/aviato.png")
    f = open(file_name, "rb")
    content = f.read()
    setup_response = client.upload_media(setup_request, content)
    f.close()
    print("Setup response: %r" % setup_response)

    assert setup_response.get("success")

    request = {
        "mediaId": setup_response["id"],
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
