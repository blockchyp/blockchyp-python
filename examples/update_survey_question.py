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
    "ordinal": 1,
    "questionText": "Would you shop here again?",
    "questionType": "yes_no",
    "enabled": True,
}

# run the transaction.
response = client.update_survey_question(request)

print("Response: %r" % response)
