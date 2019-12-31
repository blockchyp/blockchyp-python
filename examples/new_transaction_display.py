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
    "terminalName": "Test Terminal",
    "transaction": {
        "subtotal": "60.00",
        "tax": "5.00",
        "total": "65.00",
        "items": [
            {
                "description": "Leki Trekking Poles",
                "price": "35.00",
                "quantity": 2,
                "extended": "70.00",
                "discounts": [
                    {
                        "description": "memberDiscount",
                        "amount": "10.00",
                    },
                ],
            },
        ],
    },
}

# run the transaction.
response = client.new_transaction_display(request)

print("Response: %r" % response)
