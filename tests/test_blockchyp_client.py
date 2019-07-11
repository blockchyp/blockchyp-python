"""Unit and Integration tests for the BlockChyp Client"""


import blockchyp

def test_heartbeat():
    """This method tests functionality of the heartbeat method"""
    creds = blockchyp.BlockChypCredentials(
        "",
        "",
        "")
    client = blockchyp.BlockChypClient(creds, False, True)
    reply = client.heartbeat()

    assert reply["success"] is True
    assert reply["errors"] is None
    assert reply["merchantPk"]

def test_ping():
    """This method tests functionality of the ping method"""
    creds = blockchyp.BlockChypCredentials(
        "",
        "",
        "")
    client = blockchyp.BlockChypClient(creds, False, True)
    reply = client.ping("Test Terminal")

    assert reply["success"] is True
