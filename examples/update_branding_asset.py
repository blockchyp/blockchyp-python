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
    "mediaId": "<MEDIA ID>",
    "padded": True,
    "ordinal": 10,
    "startDate": "01/06/2021",
    "startTime": "14:00",
    "endDate": "11/05/2024",
    "endTime": "16:00",
    "notes": "Test Branding Asset",
    "preview": False,
    "enabled": True,
}

# run the transaction.
response = client.update_branding_asset(request)

print("Response: %r" % response)
