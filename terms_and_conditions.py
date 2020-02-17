import os

import blockchyp

# initialize a client.
client = blockchyp.Client(
    api_key=os.environ["BC_API_KEY"],
    bearer_token=os.environ["BC_BEARER_TOKEN"],
    signing_key=os.environ["BC_SIGNING_KEY"],
)

client.gateway_url = "http://localhost:8000"
client.gateway_test_url = "http://localhost:8003"

# populate request parameters.
request = {
    "test": True,
    "terminalName": "Test Terminal",

    # Alias for a Terms and Conditions template configured in the BlockChyp
    # dashboard.
    "tcAlias": "hippa",

    # Name of the contract or document if not using an alias.
    "tcName": "HIPPA Disclosure",

    # Full text of the contract or disclosure if not using an alias.
    "tcContent": "Full contract text",

    # Width of the signature image in pixels.
    "sigWidth": 200,

    # Whether or not a signature is required. Defaults to true.
    "sigRequired": True,

    "sigFile": "foo.png",
}

# run the transaction.
response = client.terms_and_conditions(request)

print("Response: %r" % response)
