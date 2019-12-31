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
    "test": True,
    "transactionId": "<PREAUTH TRANSACTION ID>",
}

# run the transaction.
response = client.capture(request)

print("Response: %r" % response)
