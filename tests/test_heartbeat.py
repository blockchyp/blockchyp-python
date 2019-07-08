import pytest

import blockchyp

def test_heartbeat():
    creds = blockchyp.BlockChypCredentials("", "", "")
    client = blockchyp.BlockChypClient(creds)
    reply = client.heartbeat()

    assert reply["success"]
    assert reply["errors"] == None