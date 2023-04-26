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
def test_tc_template():
    """Returns a single terms and conditions template."""


    terminal = _get_test_config().get("defaultTerminalName")


    client = _get_test_client("")

    setup_request = {
        "alias": str(uuid.uuid4()),
        "name": "HIPPA Disclosure",
        "content": "Lorem ipsum dolor sit amet.",
    }

    setup_response = client.tc_update_template(setup_request)
    print("Setup response: %r" % setup_response)

    assert setup_response.get("success")

    request = {
        "templateId": setup_response["id"],
    }

    response = client.tc_template(request)
    print("Response: %r" % response)

    assert response.get("success") is True
    assert response.get("name") == "HIPPA Disclosure"
    assert response.get("content") == "Lorem ipsum dolor sit amet."
