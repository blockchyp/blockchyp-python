"""This file contains unit tests for the BlockChyp Client"""


import blockchyp

def test_heartbeat():
    """This method tests functionality of the heartbeat method"""
    creds = blockchyp.BlockChypCredentials(
        "EN4S42E2KQL3FFQQ22K3LENPKQ",
        "B6KV3NXFMN6YEGW2YNHS36TEVE",
        "3fb111659a5cd66643e815db90c06bb361b50d91f97c41fe49d7cf403f343a36")
    client = blockchyp.BlockChypClient(creds)
    reply = client.heartbeat()

    assert reply["success"]
    assert reply["errors"] is None
    assert reply["merchantPk"]

# Note: Ping test disabled until CryptoUtils is implemented.
def test_ping():
    """This method tests functionality of the ping method"""
    creds = blockchyp.BlockChypCredentials(
        "EN4S42E2KQL3FFQQ22K3LENPKQ",
        "B6KV3NXFMN6YEGW2YNHS36TEVE",
        "3fb111659a5cd66643e815db90c06bb361b50d91f97c41fe49d7cf403f343a36")
    client = blockchyp.BlockChypClient(creds)
    reply = client.ping("Test Terminal")

    assert reply["success"]
