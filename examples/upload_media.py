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
    "fileName": "aviato.png",
    "fileSize": 18843,
    "uploadId": "<RANDOM ID>",
}

# run the transaction.
f = open("aviato.png", "rb")
content = f.read()
response = client.upload_media(request, content)
f.close()

print("Response: %r" % response)
