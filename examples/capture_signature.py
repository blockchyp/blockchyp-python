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

    # File format for the signature image.
    "sigFormat": blockchyp.SignatureFormat.PNG,

    # Width of the signature image in pixels.
    "sigWidth": 200,
}

# run the transaction.
response = client.capture_signature(request)

print("Response: %r" % response)
