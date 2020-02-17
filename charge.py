import os

import blockchyp

# initialize a client.
client = blockchyp.Client(
    api_key=os.environ["BC_API_KEY"],
    bearer_token=os.environ["BC_BEARER_TOKEN"],
    signing_key=os.environ["BC_SIGNING_KEY"],
)

client.gateway_url = "http://localhost:8000"
client.gateway_test_url = "http://localhost:8003"

# populate request parameters.
request = {
    "test": True,
    "terminalName": "Test Terminal",
    "amount": "55.00",
}

# run the transaction.
response = client.charge(request)

print("Response: %r" % response)
