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
    "customer": {
        "id": "<CUSTOMER ID>",
        "customerRef": "Customer reference string",
        "firstName": "FirstName",
        "lastName": "LastName",
        "companyName": "Company Name",
        "emailAddress": "notifications@blockchypteam.m8r.co",
        "smsNumber": "(123) 123-1231",
    },
}

# run the transaction.
response = client.update_customer(request)

print("Response: %r" % response)
