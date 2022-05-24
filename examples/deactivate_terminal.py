import os

import blockchyp

# initialize a client.
client = blockchyp.Client(
    api_key=os.environ["BC_API_KEY"],
    bearer_token=os.environ["BC_BEARER_TOKEN"],
    signing_key=os.environ["BC_SIGNING_KEY"],
)

# populate request parameters.
request = {
    "terminalId": str(uuid.uuid4()),
    "timeout": 120,
}

# run the transaction.
response = client.deactivate_terminal(request)

print("Response: %r" % response)
