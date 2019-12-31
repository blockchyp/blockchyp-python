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

    # Alias for a T&C template configured in blockchyp.
    "tcAlias": "hippa",

    # Name of the contract or document if not using an alias.
    "tcName": "HIPPA Disclosure",

    # Full text of the contract or disclosure if not using an alias.
    "tcContent": "Full contract text",

    # File format for the signature image, if desired can be PNG or JPG.
    "sigFormat": blockchyp.SignatureFormat.PNG,

    # Width of the signature image in pixels.
    "sigWidth": 200,

    # Whether or not a signature is required. Defaults to true.
    "sigRequired": True,
}

# run the transaction.
response = client.tc(request)

print("Response: %r" % response)
