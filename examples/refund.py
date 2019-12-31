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
    "terminalName": "Test Terminal",
    "transactionId": "<PREVIOUS TRANSACTION ID>",

    # Optional amount for partial refunds.
    "amount": "5.00",
}

# run the transaction.
response = client.refund(request)

print("Response: %r" % response)
