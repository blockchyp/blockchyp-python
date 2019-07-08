"""This file contains unit tests for the BlockChypClient heartbeat method"""


import blockchyp

def test_heartbeat():
    """This method tests functionality of the heartbeat method"""
    creds = blockchyp.BlockChypCredentials("", "", "")
    client = blockchyp.BlockChypClient(creds)
    reply = client.heartbeat()

    assert reply["success"]
    assert reply["errors"] is None
