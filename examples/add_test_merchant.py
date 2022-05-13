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
    "dbaName": "DBA name.",
    "companyName": "test merchant customer name.",
}

# run the transaction.
response = client.add_test_merchant(request)

print("Response: %r" % response)
