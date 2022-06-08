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
    "merchantId": "<MERCHANT ID>",
    "test": True,
    "dbaName": "Test Merchant",
    "companyName": "Test Merchant",
    "billingAddress": {
        "address1": "1060 West Addison",
        "city": "Chicago",
        "stateOrProvince": "IL",
        "postalCode": "60613",
    },
}

# run the transaction.
response = client.update_merchant(request)

print("Response: %r" % response)
