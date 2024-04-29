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
def test_update_survey_question():
    """Update or create a survey question."""


    terminal = _get_test_config().get("defaultTerminalName")


    client = _get_test_client("")

    request = {
        "ordinal": 1,
        "questionText": "Would you shop here again?",
        "questionType": "yes_no",
    }

    response = client.update_survey_question(request)
    print("Response: %r" % response)

    assert response.get("success") is True
    assert response.get("questionText") == "Would you shop here again?"
    assert response.get("questionType") == "yes_no"
