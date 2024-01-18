# Copyright 2019-2024 BlockChyp, Inc. All rights reserved. Use of this code is
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
def test_delete_survey_question():
    """Delete a survey question."""


    terminal = _get_test_config().get("defaultTerminalName")


    client = _get_test_client("")

    setup_request = {
        "ordinal": 1,
        "questionText": "Would you shop here again?",
        "questionType": "yes_no",
    }

    setup_response = client.update_survey_question(setup_request)
    print("Setup response: %r" % setup_response)

    assert setup_response.get("success")

    request = {
        "questionId": setup_response["id"],
    }

    response = client.delete_survey_question(request)
    print("Response: %r" % response)

    assert response.get("success") is True
