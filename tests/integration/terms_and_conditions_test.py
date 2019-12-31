# Copyright 2019 BlockChyp, Inc. All rights reserved. Use of this code is
# governed by a license that can be found in the LICENSE file.
#
# This file was generated automatically. Changes to this file will be lost every
# time the code is regenerated.
import pytest

import blockchyp

from .util import _get_test_client


@pytest.mark.itest
def test_terms_and_conditions():
    """Can capture terms and conditions acceptance."""

    client = _get_test_client()

    request = {
        "test": True,
        "terminalName": "Test Terminal",
        "tcName": "HIPPA Disclosure",
        "tcContent": "Full contract text",
        "sigFormat": blockchyp.SignatureFormat.PNG,
        "sigWidth": 200,
        "sigRequired": True,
    }

    response = client.terms_and_conditions(request)

    print("Response: %r" % response)

    assert response.get("success") is True

