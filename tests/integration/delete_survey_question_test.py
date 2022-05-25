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
def test_delete_survey_question():
    """Delete a survey question."""

    client = _get_test_client()
    terminal = _get_test_config().get("defaultTerminalName")

    delay = os.environ.get("BC_TEST_DELAY")
    if delay:
        client.message({
            "terminalName": terminal,
            "test": True,
            "message": f"Running delete_survey_question in {delay}s",
        })
        time.sleep(int(delay))


    setup_request = {
        "ordinal": 1,
        "questionText": "Would you shop here again?",
        "questionType": "yes_no",
    }

    setup_response = client.update_survey_question(setup_request)

    print("Setup response: %r" % setup_response)

    assert setup_response.get("success")

    request = {
        "questionId": ,
    }

    response = client.delete_survey_question(request)

    print("Response: %r" % response)

    assert response.get("success") is True
