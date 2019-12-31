# Copyright 2019 BlockChyp, Inc. All rights reserved. Use of this code is
# governed by a license that can be found in the LICENSE file.
#
# This file was generated automatically. Changes to this file will be lost every
# time the code is regenerated.
import pytest

import blockchyp

from .util import _get_test_client


@pytest.mark.itest
def test_boolean_prompt():
    """Can prompt the consumer for boolean input."""

    client = _get_test_client()

    request = {
        "test": True,
        "terminalName": "Test Terminal",
        "prompt": "Would you like to become a member?",
        "yesCaption": "Yes",
        "noCaption": "No",
    }

    response = client.boolean_prompt(request)

    print("Response: %r" % response)

    assert response.get("success") is True
    assert response.get("response") is True

