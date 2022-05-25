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
    "questionId": "<SURVEY QUESTION ID>",
}

# run the transaction.
response = client.survey_results(request)

print("Response: %r" % response)
