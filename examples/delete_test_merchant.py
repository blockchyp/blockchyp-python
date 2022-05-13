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
    "merchantId": "ID for the test merchant being deleted.",
}

# run the transaction.
response = client.delete_test_merchant(request)

print("Response: %r" % response)
