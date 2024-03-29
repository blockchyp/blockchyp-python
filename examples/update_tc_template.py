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
    "alias": "HIPPA",
    "name": "HIPPA Disclosure",
    "content": "Lorem ipsum dolor sit amet.",
    "timeout": 120,
}

# run the transaction.
response = client.update_tc_template(request)

print("Response: %r" % response)
