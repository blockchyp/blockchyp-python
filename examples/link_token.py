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
    "token": "Token to link",
    "customerId": "Customer to link",
}

# run the transaction.
response = client.link_token(request)

print("Response: %r" % response)