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
    "amount": "199.99",
    "description": "Widget",
    "subject": "Widget invoice",
    "transaction": {
        "subtotal": "195.00",
        "tax": "4.99",
        "total": "199.99",
        "items": [
            {
                "description": "Widget",
                "price": "195.00",
                "quantity": 1,
            },
        ],
    },
    "autoSend": True,
    "customer": {
        "customerRef": "Customer reference string",
        "firstName": "FirstName",
        "lastName": "LastName",
        "companyName": "Company Name",
        "emailAddress": "support@blockchyp.com",
        "smsNumber": "(123) 123-1231",
    },
}

# run the transaction.
response = client.send_payment_link(request)

print("Response: %r" % response)
