# Copyright 2019-2026 BlockChyp, Inc. All rights reserved. Use of this code is
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
def test_tc_log():
    """Returns Terms and Conditions log entries."""


    terminal = _get_test_config().get("defaultTerminalName")


    client = _get_test_client("")

    setup_request = {
        "test": True,
        "terminalName": terminal,
        "tcName": "HIPPA Disclosure",
        "tcContent": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ullamcorper id urna quis pulvinar. Pellentesque vestibulum justo ac nulla consectetur tristique. Suspendisse arcu arcu, viverra vel luctus non, dapibus vitae augue. Aenean ac volutpat purus. Curabitur in lacus nisi. Nam vel sagittis eros. Curabitur faucibus ut nisl in pulvinar. Nunc egestas, orci ut porttitor tempus, ante mauris pellentesque ex, nec feugiat purus arcu ac metus. Cras sodales ornare lobortis. Aenean lacinia ultricies purus quis pharetra. Cras vestibulum nulla et magna eleifend eleifend. Nunc nibh dolor, malesuada ut suscipit vitae, bibendum quis dolor. Phasellus ultricies ex vitae dolor malesuada, vel dignissim neque accumsan.",
        "sigFormat": blockchyp.SignatureFormat.PNG,
        "sigWidth": 200,
        "sigRequired": True,
    }

    setup_response = client.terms_and_conditions(setup_request)
    print("Setup response: %r" % setup_response)

    assert setup_response.get("success")

    request = {
    }

    response = client.tc_log(request)
    print("Response: %r" % response)

    assert response.get("success") is True
