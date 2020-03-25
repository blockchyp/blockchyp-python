# BlockChyp Python SDK

[![Build Status](https://circleci.com/gh/blockchyp/blockchyp-python/tree/master.svg?style=shield)](https://circleci.com/gh/blockchyp/blockchyp-python/tree/master)
[![PyPI](https://img.shields.io/pypi/v/blockchyp.svg)](https://pypi.org/project/blockchyp/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/blockchyp/blockchyp-python/blob/master/LICENSE)

The official library for accessing the [BlockChyp] Terminal and Gateway APIs
from Python.

## Installation

BlockChyp can be simply installed by running:

```sh
pip install blockchyp
```


## The Rest APIs

All BlockChyp SDKs provide a convenient way of accessing the BlockChyp REST APIs.
You can checkout the REST API documentation via the links below.

[Terminal REST API Docs](https://docs.blockchyp.com/rest-api/terminal/index.html)

[Gateway REST API Docs](https://docs.blockchyp.com/rest-api/gateway/index.html)

## Other SDKs

BlockChyp has officially supported SDKs for eight different development platforms and counting.
Here's the full list with links to their GitHub repositories.

[Go SDK](https://github.com/blockchyp/blockchyp-go)

[Node.js/JavaScript SDK](https://github.com/blockchyp/blockchyp-js)

[Java SDK](https://github.com/blockchyp/blockchyp-java)

[.net/C# SDK](https://github.com/blockchyp/blockchyp-csharp)

[Ruby SDK](https://github.com/blockchyp/blockchyp-ruby)

[PHP SDK](https://github.com/blockchyp/blockchyp-php)

[Python SDK](https://github.com/blockchyp/blockchyp-python)

[iOS (Objective-C/Swift) SDK](https://github.com/blockchyp/blockchyp-ios)

## Getting a Developer Kit

In order to test your integration with real terminals, you'll need a BlockChyp
Developer Kit. Our kits include a fully functioning payment terminal with
test pin encryption keys. Every kit includes a comprehensive set of test
cards with test cards for every major card brand and entry method, including
Contactless and Contact EMV and mag stripe cards. Each kit also includes
test gift cards for our blockchain gift card system.

Access to BlockChyp's developer program is currently invite only, but you
can request an invitation by contacting our engineering team at **nerds@blockchyp.com**.

You can also view a number of long form demos and learn more about us on our [YouTube Channel](https://www.youtube.com/channel/UCE-iIVlJic_XArs_U65ZcJg).

## Transaction Code Examples

You don't want to read words. You want examples. Here's a quick rundown of the
stuff you can do with the BlockChyp Python SDK and a few basic examples.

#### Charge

Executes a standard direct preauth and capture.


```python
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
    "amount": "55.00",
}

# run the transaction.
response = client.charge(request)

print("Response: %r" % response)


```

#### Preauthorization

Executes a preauthorization intended to be captured later.


```python
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
    "amount": "27.00",
}

# run the transaction.
response = client.preauth(request)

print("Response: %r" % response)


```

#### Terminal Ping

Tests connectivity with a payment terminal.


```python
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
}

# run the transaction.
response = client.ping(request)

print("Response: %r" % response)


```

#### Balance

Checks the remaining balance on a payment method.


```python
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
    "cardType": blockchyp.CardType.EBT,
}

# run the transaction.
response = client.balance(request)

print("Response: %r" % response)


```

#### Terminal Clear

Clears the line item display and any in progress transaction.


```python
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
}

# run the transaction.
response = client.clear(request)

print("Response: %r" % response)


```

#### Terms & Conditions Capture

Prompts the user to accept terms and conditions.


```python
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

    # Alias for a Terms and Conditions template configured in the BlockChyp
    # dashboard.
    "tcAlias": "hippa",

    # Name of the contract or document if not using an alias.
    "tcName": "HIPPA Disclosure",

    # Full text of the contract or disclosure if not using an alias.
    "tcContent": "Full contract text",

    # File format for the signature image.
    "sigFormat": blockchyp.SignatureFormat.PNG,

    # Width of the signature image in pixels.
    "sigWidth": 200,

    # Whether or not a signature is required. Defaults to true.
    "sigRequired": True,
}

# run the transaction.
response = client.terms_and_conditions(request)

print("Response: %r" % response)


```

#### Update Transaction Display

Appends items to an existing transaction display.  Subtotal, Tax, and Total are
overwritten by the request. Items with the same description are combined into
groups.


```python
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
response = client.update_transaction_display(request)

print("Response: %r" % response)


```

#### New Transaction Display

Displays a new transaction on the terminal.


```python
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


```

#### Text Prompt

Asks the consumer a text based question.


```python
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

    # Type of prompt. Can be 'email', 'phone', 'customer-number', or
    # 'rewards-number'.
    "promptType": blockchyp.PromptType.EMAIL,
}

# run the transaction.
response = client.text_prompt(request)

print("Response: %r" % response)


```

#### Boolean Prompt

Asks the consumer a yes/no question.


```python
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
    "prompt": "Would you like to become a member?",
    "yesCaption": "Yes",
    "noCaption": "No",
}

# run the transaction.
response = client.boolean_prompt(request)

print("Response: %r" % response)


```

#### Display Message

Displays a short message on the terminal.


```python
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
    "message": "Thank you for your business.",
}

# run the transaction.
response = client.message(request)

print("Response: %r" % response)


```

#### Refund

Executes a refund.


```python
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
    "transactionId": "<PREVIOUS TRANSACTION ID>",

    # Optional amount for partial refunds.
    "amount": "5.00",
}

# run the transaction.
response = client.refund(request)

print("Response: %r" % response)


```

#### Enroll

Adds a new payment method to the token vault.


```python
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
}

# run the transaction.
response = client.enroll(request)

print("Response: %r" % response)


```

#### Gift Card Activation

Activates or recharges a gift card.


```python
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
    "amount": "50.00",
}

# run the transaction.
response = client.gift_activate(request)

print("Response: %r" % response)


```

#### Time Out Reversal

Executes a manual time out reversal.

We love time out reversals. Don't be afraid to use them whenever a request to a
BlockChyp terminal times out. You have up to two minutes to reverse any
transaction. The only caveat is that you must assign transactionRef values when
you build the original request. Otherwise, we have no real way of knowing which
transaction you're trying to reverse because we may not have assigned it an id
yet. And if we did assign it an id, you wouldn't know what it is because your
request to the terminal timed out before you got a response.


```python
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
    "transactionRef": "<LAST TRANSACTION REF>",
}

# run the transaction.
response = client.reverse(request)

print("Response: %r" % response)


```

#### Capture Preauthorization

Captures a preauthorization.


```python
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
    "transactionId": "<PREAUTH TRANSACTION ID>",
}

# run the transaction.
response = client.capture(request)

print("Response: %r" % response)


```

#### Close Batch

Closes the current credit card batch.


```python
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
}

# run the transaction.
response = client.close_batch(request)

print("Response: %r" % response)


```

#### Void Transaction

Discards a previous preauth transaction.


```python
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
    "transactionId": "<PREVIOUS TRANSACTION ID>",
}

# run the transaction.
response = client.void(request)

print("Response: %r" % response)


```

#### Terminal Status

Returns the current status of a terminal.


```python
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
}

# run the transaction.
response = client.terminal_status(request)

print("Response: %r" % response)


```

#### Capture Signature.

Captures and returns a signature.


```python
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


```

#### Update Customer

Updates or creates a customer record.


```python
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
    "customer": {
        "id": "ID of the customer to update",
        "customerRef": "Customer reference string",
        "firstName": "FirstName",
        "lastName": "LastName",
        "companyName": "Company Name",
        "emailAddress": "support@blockchyp.com",
        "smsNumber": "(123) 123-1231",
    },
}

# run the transaction.
response = client.update_customer(request)

print("Response: %r" % response)


```

#### Retrieve Customer

Retrieves a customer by id.


```python
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
    "customerId": "ID of the customer to retrieve",
}

# run the transaction.
response = client.customer(request)

print("Response: %r" % response)


```

#### Search Customer

Searches the customer database.


```python
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
    "query": "(123) 123-1234",
}

# run the transaction.
response = client.customer_search(request)

print("Response: %r" % response)


```

#### Transaction Status

Retrieves the current status of a transaction.


```python
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
    "transactionId": "ID of transaction to retrieve",
}

# run the transaction.
response = client.transaction_status(request)

print("Response: %r" % response)


```

#### Send Payment Link

Creates and send a payment link to a customer.


```python
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


```

## Running Integration Tests

If you'd like to run the integration tests, create a new file on your system
called `sdk-itest-config.json` with the API credentials you'll be using as
shown in the example below.

```
{
 "gatewayHost": "https://api.blockchyp.com",
 "testGatewayHost": "https://test.blockchyp.com",
 "apiKey": "PZZNEFK7HFULCB3HTLA7HRQDJU",
 "bearerToken": "QUJCHIKNXOMSPGQ4QLT2UJX5DI",
 "signingKey": "f88a72d8bc0965f193abc7006bbffa240663c10e4d1dc3ba2f81e0ca10d359f5"
}
```

This file can be located in a few different places, but is usually located
at `<USER_HOME>/.config/blockchyp/sdk-itest-config.json`. All BlockChyp SDKs
use the same configuration file.

To run the integration test suite via `make`, type the following command:

`make integration`

[BlockChyp]: https://www.blockchyp.com

## Contributions

BlockChyp welcomes contributions from the open source community, but bear in mind
that this repository has been generated by our internal SDK Generator tool. If
we choose to accept a PR or contribution, your code will be moved into our SDK
Generator project, which is a private repository.

## License

Copyright BlockChyp, Inc., 2019

Distributed under the terms of the [MIT] license, blockchyp-python is free and open source software.

[MIT]: https://github.com/blockchyp/blockchyp-python/blob/master/LICENSE
