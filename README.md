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


## Additional Documentation

Complete documentation can be found on our [Developer Documentation Portal].

[Developer Documentation Portal]: https://docs.blockchyp.com/

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

#### Terminal Ping


This simple test transaction helps ensure you have good communication with a payment terminal and is usually the first one you'll run in development.

It tests communication with the terminal and returns a positive response if everything
is okay.  It works the same way in local or cloud relay mode.

If you get a positive response, you've successfully verified all of the following:

* The terminal is online.
* There is a valid route to the terminal.
* The API Credentials are valid.




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

#### Charge


Our most popular transaction executes a standard authorization and capture.
This is the most basic of
basic payment transactions, typically used in conventional retail.

Charge transactions can use a payment terminal to capture a payment or
use a previously enrolled payment token.

**Terminal Transactions**

For terminal transactions, make sure you pass in the terminal name using the `terminalName` property.

**Token Transactions**

If you have a payment token, omit the `terminalName` property and pass in the token with the `token`
property instead.

**Card Numbers and Mag Stripes**

You can also pass in PANs and Mag Stripes, but you probably shouldn't. This will
put you in PCI scope and the most common vector for POS breaches is key logging.
If you use terminals for manual card entry, you'll bypass any key loggers that
might be maliciously running on the point-of-sale system.

**Common Variations**

* **Gift Card Redemption**:  There's no special API for gift card redemption in BlockChyp. Just execute a plain charge transaction and if the customer happens to swipe a gift card, our terminals will identify the gift card and run a gift card redemption. Also note that if for some reason the gift card's original purchase transaction is associated with fraud or a chargeback, the transaction will be rejected.
* **EBT**: Set the `card_type` field to `blockchyp.CardType.EBT` to process an EBT SNAP transaction. Note that test EBT transactions always assume a balance of $100.00, so test EBT transactions over that amount may be declined.
* **Cash Back**: To enable cash back for debit transactions, set the `cash_back` field. If the card presented isn't a debit card, the `cash_back` field will be ignored.
* **Manual Card Entry**: Set the `manual_entry` field to enable manual card entry. Good as a backup when chips and MSR's don't work or for more secure phone orders. You can even combine the `manual_entry` field with the `card_type` field set to `blockchyp.CardType.EBT` for manual EBT card entry.
* **Inline Tokenization**: You can enroll the payment method in the token vault inline with a charge transaction by setting the `enroll` field. You'll get a token back in the response. You can even bind the token to a customer record if you also pass in customer data.
* **Prompting for Tips**: Set the `prompt_for_tip` field if you'd like to prompt the customer for a tip before authorization. Good for pay-at-the-table and other service related scenarios.
* **Cash Discounting and Surcharging**:  The `surcharge` and `cash_discount` fields can be used together to support cash discounting or surcharge problems. Consult the Cash Discount documentation for more details.




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


A preauthorization puts a hold on funds and must be captured later.  This is used
in scenarios where the final transaction amount might change.  A common examples would
be fine dining where a tip adjustment is required prior to final settlement.

Another use case for preauthorization is e-commerce.  Typically, an online order
is preauthorized at the time of the order and then captured when the order ships.

Preauthorizations can use a payment terminal to capture a payment or
use a previously enrolled payment token.

**Terminal Transactions**

For terminal transactions, make sure you pass in the terminal name using the `terminalName` property.

**Token Transactions**

If you have a payment token, omit the `terminalName` property and pass in the token with the `token`
property instead.

**Card Numbers and Mag Stripes**

You can also pass in PANs and Mag Stripes, but you probably shouldn't.  This will
put you in PCI scope and the most common vector for POS breaches is key logging.
If you use terminals for manual card entry, you'll bypass any key loggers that
might be maliciously running on the point-of-sale system.

**Common Variations**

* **Manual Card Entry**: Set the `manual_entry` field to enable manual card entry. Good as a backup when chips and MSR's don't work or for more secure phone orders. You can even combine the `manual_entry` field with `card_type` set to `blockchyp.CardType.EBT` for manual EBT card entry.
* **Inline Tokenization**: You can enroll the payment method in the token vault in line with a charge transaction by setting the `enroll` field. You'll get a token back in the response. You can even bind the token to a customer record if you also pass in customer data.
* **Prompting for Tips**: Set the `prompt_for_tip` field if you'd like to prompt the customer for a tip before authorization. You can prompt for tips as part of a preauthorization, although it's not a very common approach.
* **Cash Discounting and Surcharging**: The `surcharge` and `cash_discount` fields can be used together to support cash discounting or surcharge problems. Consult the Cash Discount documentation for more details.




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

#### Capture Preauthorization


This API allows you to capture a previously approved preauthorization.

You'll need to make sure you pass in the Transaction ID returned by the original preauth transaction so we know which transaction we're capturing.  If you want to capture the transaction for the
exact amount of the preauth, the Transaction ID is all you need to pass in.

You can adjust the total if you need to by passing in a new `amount`.  We
also recommend you pass in updated amounts for `tax` and `tip` as it can
reduce your interchange fees in some cases. (Level II Processing, for example.)




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

#### Refund


It's not ideal, but sometimes customers want their money back.

Our refund API allows you to confront this unpleasant reality by executing refunds in a few different scenarios.

The most fraud resistent method is to execute refunds in the context of a previous transaction.  You should always keep track of the Transaction ID
returned in a BlockChyp response.  To refund the full amount of the previous transaction, just pass in the original Transaction ID with the refund requests.

**Partial Refunds**

For a partial refund, just pass in an amount along with the Transaction ID.
The only rule is that the amount has to be equal to or less than the original
transaction.  You can execute multiple partial refunds against the same
original transaction as long as the total refunded amount doesn't exceed the original amount.

**Tokenized Refunds**

You can also use a token to execute a refund.  Pass in a token instead
of the Transaction ID along with the desired refund amount.

**Free Range Refunds**

When you execute a refund without referencing a previous transaction, we
call this a *free range refund*.

We don't recommend it, but it is permitted.  If you absolutely insist on
doing it, pass in a Terminal Name and an amount.

You can execute a manual or keyed refund by passing the `manual_entry` field
to a free range refund request.

**Gift Card Refunds**

Gift card refunds are allowed in the context of a previous transaction, but
free range gift card refunds are not allowed.  Use the gift card activation
API if you need to add more funds to a gift card.

**Store and Forward Support**

Refunds are not permitted when a terminal falls back to store and forward mode.

**Auto Voids**

If a refund referencing a previous transaction is executed for the full amount
before the original transaction's batch is closed, the refund is automatically
converted to a void.  This saves the merchant a little bit of money.




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
    "transactionId": "<PREVIOUS TRANSACTION ID>",

    # Optional amount for partial refunds.
    "amount": "5.00",
}

# run the transaction.
response = client.refund(request)

print("Response: %r" % response)


```

#### Enroll


This API allows you to tokenize and enroll a payment method in the token
vault.  You can also pass in customer information and associate the
payment method with a customer record.

A token is returned in the response that can be used in subsequent charge,
preauth, and refund transactions.

**Gift Cards and EBT**

Gift Cards and EBT cards cannot be tokenized.

**E-Commerce Tokens**

The tokens returned by the enroll API and the e-commerce web tokenizer
are the same tokens and can be used interchangeably.




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

#### Void



Mistakes happen.  If a transaction is made by mistake, you can void it
with this API.  All that's needed is to pass in a Transaction ID and execute
the void before the original transaction's batch closes.

Voids work with EBT and gift card transactions with no additional parameters.




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

#### Time Out Reversal



Payment transactions require a stable network to function correctly and
no network is stable all the time.  Time out reversals are a great line
of defense against accidentally double charging consumers when payments
are retried during shaky network conditions.

We highly recommend developers use this API whenever a charge, preauth, or refund transaction times out.  If you don't receive a definitive response
from BlockChyp, you can't be certain about whether or not the transaction went through.

The best practice in this situation is to send a time out reversal request.  Time out reversals check for a transaction and void it if it exists.

The only caveat is that developers must use the `transactionRef` property (`txRef` for the CLI) when executing charge, preauth, and refund transactions.

The reason for this requirement is that if a system never receives a definitive
response for a transaction, the system would never have received the BlockChyp
generated Transaction ID.  We have to fallback to Transaction Ref to identify
a transaction.




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
    "transactionRef": "<LAST TRANSACTION REF>",
}

# run the transaction.
response = client.reverse(request)

print("Response: %r" % response)


```

#### Gift Card Activation


This API can be used to activate or add value to BlockChyp gift cards.
Just pass in the terminal name and the amount to add to the card.
Once the customer swipes their card, the terminal will use keys
on the mag stripe to add value to the card.

You don't need to handle a new gift card activation or a gift card recharge any
differently.  The terminal firmware will figure out what to do on its
own and also returns the new balance for the gift card.

This is the part of the system where BlockChyp's blockchain DNA comes
closest to the surface.  The BlockChyp gift card system doesn't really
use gift card numbers.  This means they can't be stolen.

BlockChyp identifies cards with an elliptic curve public key instead.
Gift card transactions are actually blocks signed with those keys.
This means there are no shared secrets sent over the network.
To keep track of a BlockChyp gift card, hang on to the **public key** returned
during gift card activation.  That's the gift card's elliptic curve public key.

We sometimes print numbers on our gift cards, but these are actually
decimal encoded hashes of a portion of the public key to make our gift
cards seem *normal* to *normies*.  They can be used
for balance checks and play a lookup role in online gift card
authorization, but are of little use beyond that.

**Voids and Reversals**

Gift card activations can be voided and reversed just like any other
BlockChyp transaction.  Use the Transaction ID or Transaction Ref
to identify the gift activation transaction as you normally would for
voiding or reversing a conventional payment transaction.

**Importing Gift Cards**

BlockChyp does have the ability to import gift card liability from
conventional gift card platforms.  Unfortunately, BlockChyp does not
support activating cards on third party systems, but you can import
your outstanding gift cards and customers can swipe them on the
terminals just like BlockChyp's standard gift cards.

No special coding is required to access this feature.  The gateway and
terminal firmware handle everything for you.

**Third Party Gift Card Networks**

BlockChyp does not currently provide any native support for other gift card
platforms beyond importing gift card liability.  We do have a white listing system
that can be used to support your own custom gift card implementations.  We have a security review
process before we allow a BIN range to be white listed, so contact
support@blockchyp.com if you need to white list a BIN range.




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

#### Balance



Checks a gift or EBT card balance.

**Gift Card Balance Checks**

For gift cards, just pass in a terminal name and the customer will be prompted
to swipe a card on that terminal.  The remaining balance will be displayed
briefly on the terminal screen and the API response will include the gift card's public key and the remaining balance.

**EBT Balance Checks**

All EBT transactions require a PIN, so in order to check an EBT card balance,
you need to pass in the `ebt` flag just like you would for a normal EBT
charge transaction.  The customer will be prompted to swipe their card and
enter a PIN code.  If everything checks out, the remaining balance on the card will be displayed on the terminal for the customer and returned in the API.

**Testing Gift Card Balance Checks**

Test gift card balance checks work no differently than live gift cards.  You
must activate a test gift card first in order to test balance checks.  Test
gift cards are real blockchain cards that live on our parallel test blockchain.

**Testing EBT Gift Card Balance Checks**

All test EBT transactions assume a starting balance of $100.00.  As a result,
test EBT balance checks always return a balance of $100.00.




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

#### Close Batch


This API will close the merchant's batch if it's currently open.

By default, merchant batches will close automatically at 3 AM in their
local time zone.  The automatic batch closure time can be changed
in the Merchant Profile or disabled completely.

If automatic batch closure is disabled, you'll need to use this API to
close the batch manually.



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

#### Send Payment Link



This API allows you to send an invoice to a customer and capture payment
via a BlockChyp hosted payment page.

If you set the `autoSend` flag, BlockChyp will send a basic invoice email
to the customer for you that includes the payment link.  If you'd rather have
more control over the look of the email message, you can omit the `autoSend`
flag and send the customer email yourself.

There are a lot of optional parameters for this API, but at a minimum
you'll need to pass in a total, customer name, and email address. (Unless
you use the `cashier` flag.)

**Customer Info**

Unless you're using the `cashier` flag, you must specify a customer, either by
creating a new customer record inline or by passing in an existing Customer ID or Customer Ref.

**Line Item Level Data**

It's not strictly required, but we strongly recommend sending line item level
detail with every request.  It will make the invoice look a little more complete
and the data format for line item level data is the exact same format used
for terminal line item display, so the same code can be used to support both areas.

**Descriptions**

You can also provide a free form description or message that's displayed near
the bottom of the invoice.  Usually this is some kind of thank you note
or instruction.

**Terms and Conditions**

You can include long form contract language with a request and capture
terms and conditions acceptance at the same time payment is captured.

The interface is identical to that used for the terminal based Terms and
Conditions API in that you can pass in content directly via `tcContent` or via
a preconfigured template via `tcAlias`.  The Terms and Conditions log will also be updated when
agreement acceptance is incorporated into a send link request.

**Auto Send**

BlockChyp does not send the email notification automatically.  This is
a safeguard to prevent real emails from going out when you may not expect it.
If you want BlockChyp to send the email for you, just add the `autoSend` flag with
all requests.

**Tokenization**

Add the `enroll` flag to a send link request to enroll the payment method
in the token vault.

**Cashier Facing Card Entry**

BlockChyp can be used to generate internal/cashier facing card entry pages as well.  This is
designed for situations where you might need to take a phone order and you don't
have a terminal.

If you pass in the `cashier` flag, no email will be sent and you'll be be able to
load the link in a browser or iframe for payment entry.  When the `cashier` flag
is used, the `autoSend` flag will be ignored.

**Payment Notifications**

When a customer successfully submits payment, the merchant will receive an email
notifying them that the payment was received.

**Real Time Callback Notifications**

Email notifications are fine, but you may want your system to be informed
immediately whenever a payment event occurs.  By using the optional `callbackUrl` request
property, you can specify a URL to which the Authorization Response will be posted
every time the user submits a payment, whether approved or otherwise.

The response will be sent as a JSON encoded POST request and will be the exact
same format as all BlockChyp charge and preauth transaction responses.

**Status Polling**

If real time callbacks aren't practical or necessary in your environment, you can
always use the Transaction Status API described below.

A common use case for the send link API with status polling is curbside pickup.
You could have your system check the Transaction Status when a customer arrives to
ensure it's been paid without necessarily needing to create background threads
to constantly poll for status updates.




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

#### Transaction Status



Returns the current status for any transaction.  You can lookup a transaction
by its BlockChyp assigned Transaction ID or your own Transaction Ref.

You should alway use globally unique Transaction Ref values, but in the event
that you duplicate Transaction Refs, the most recent transaction matching your
Transaction Ref is returned.




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

#### Terminal Clear



This API interrupts whatever a terminal may be doing and returns it to the
idle state.





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

#### Terminal Status



Returns the current status of a payment terminal.  This is typically used
as a way to determine if the terminal is busy before sending a new transaction.

If the terminal is busy, `idle` will be false and the `status` field will return
a short string indicating the transaction type currently in progress.  The system
will also return the timestamp of the last status change in the `since` field.

If the system is running a payment transaction and you wisely passed in a
Transaction Ref, this API will also return the Transaction Ref of the in progress
transaction.




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

#### Terms & Conditions Capture



This API allows you to prompt a customer to accept a legal agreement on the terminal
and (usually) capture their signature.

Content for the agreement can be specified in two ways.  You can reference a
previously configured T&C template or pass in the full agreement text with every request.

**Using Templates**

If your application doesn't keep track of agreements you can leverage BlockChyp's
template system.  You can create any number of T&C Templates in the merchant dashboard
and pass in the `tcAlias` flag to specify which one to display.

**Raw Content**

If your system keeps track of the agreement language or executes complicated merging
and rendering logic, you can bypass our template system and pass in the full text with
every transaction.  Use the `tcName` to pass in the agreement name and `tcContent` to
pass in the contract text.  Note that only plain text is supported.

**Bypassing Signatures**

Signature images are captured by default.  If for some reason this doesn't fit your
use case and you'd like to capture acceptance without actually capturing a signature image, set
the `disableSignature` flag in the request.

**Terms & Conditions Log**

Every time a user accepts an agreement on the terminal, the signature image (if captured),
will be uploaded to the gateway and added to the log along with the full text of the
agreement.  This preserves the historical record in the event that standard agreements
or templates change over time.

**Associating Agreements with Transactions**

To associate a Terms & Conditions log entry with a transaction, just pass in the
Transaction ID or Transaction Ref for the associated transaction.





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

#### Capture Signature



This endpoint captures a written signature from the terminal and returns the
image.

Unlike the Terms & Conditions API, this endpoint performs basic signature
capture with no agreement display or signature archival.

Under the hood, signatures are captured in a proprietary vector format and
must be converted to a common raster format in order to be useful to most
applications.  At a minimum, you must specify an image format using the
`sigFormat` parameter.  As of this writing JPG and PNG are supported.

By default, images are returned in the JSON response as hex encoded binary.
You can redirect the binary image output to a file using the `sigFile`
parameter.

You can also scale the output image to your preferred width by
passing in a `sigWidth` parameter.  The image will be scaled to that
width, preserving the aspect ratio of the original image.




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

#### New Transaction Display



Sends totals and line item level data to the terminal.

At a minimum, you should send total information as part of a display request,
including `total`, `tax`, and `subtotal`.

You can also send line item level data and each line item can have a `description`,
`qty`, `price`, and `extended` price.

If you fail to send an extended price, BlockChyp will multiply the `qty` by the
`price`, but we strongly recommend you precalculate all the fields yourself
to ensure consistency.  Your treatment of floating-point multiplication and rounding
may differ slightly from BlockChyp's, for example.

**Discounts**

You have the option to show discounts on the display as individual line items
with negative values or you can associate discounts with a specific line item.
You can apply any number of discounts to an individual line item with a description
and amount.




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

#### Update Transaction Display



Similar to *New Transaction Display*, this variant allows developers to update
line item level data currently being displayed on the terminal.

This is designed for situations where you want to update the terminal display as
items are scanned.  This variant means you only have to send information to the
terminal that's changed, which usually means the new line item and updated totals.

If the terminal is not in line item display mode and you invoke this endpoint,
the first invocation will behave like a *New Transaction Display* call.

At a minimum, you should send total information as part of a display request,
including `total`, `tax`, and `subtotal`.

You can also send line item level data and each line item can have a `description`,
`qty`, `price`, and `extended` price.

If you fail to send an extended price, BlockChyp will multiply the `qty` by the
`price`, but we strongly recommend you precalculate all the fields yourself
to ensure consistency.  Your treatment of floating-point multiplication and rounding
may differ slightly from BlockChyp's, for example.

**Discounts**

You have the option to show discounts on the display as individual line items
with negative values or you can associate discounts with a specific line item.
You can apply any number of discounts to an individual line item with a description
and amount.




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

#### Display Message



Displays a message on the payment terminal.

Just specify the target terminal and the message using the `message` parameter.




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

#### Boolean Prompt



Prompts the customer to answer a yes or no question.

You can specify the question or prompt with the `prompt` parameter and
the response is returned in the `response` field.

This can be used for a number of use cases including starting a loyalty enrollment
workflow or customer facing suggestive selling prompts.

**Custom Captions**

You can optionally override the "YES" and "NO" button captions by
using the `yesCaption` and `noCaption` request parameters.




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

#### Text Prompt



Prompts the customer to enter numeric or alphanumeric data.

Due to PCI rules, free form prompts are not permitted when the response
could be any valid string.  The reason for this is that a malicious
developer (not you, of course) could use text prompts to ask the customer to
input a card number or PIN code.

This means that instead of providing a prompt, you provide a `promptType` instead.

The prompt types currently supported are listed below:

* **phone**: Captures a phone number.
* **email**: Captures an email address.
* **first-name**: Captures a first name.
* **last-name**: Captures a last name.
* **customer-number**: Captures a customer number.
* **rewards-number**: Captures a rewards number.

You can specify the prompt with the `promptType` parameter and
the response is returned in the `response` field.





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

#### Update Customer



Adds or updates a customer record.

If you pass in customer information including `firstName`, `lastName`, `email`,
or `sms` without any Customer ID or Customer Ref, a new record will
be created.

If you pass in `customerRef` and `customerId`, the customer record will be updated
if it exists.

**Customer Ref**

The `customerRef` field is optional, but highly recommended as this allows you
to use your own customer identifiers instead of storing BlockChyp's Customer IDs
in your systems.

**Creating Customer Records With Payment Transactions**

If you have customer information available at the time a payment transaction is
executed, you can pass all the same customer information directly into a payment transaction and
create a customer record at the same time payment is captured.  The advantage of this approach is
that the customer's payment card is automatically associated with the customer record in a single step.
If the customer uses the payment card in the future, the customer data will automatically
be returned without needing to ask the customer to provide any additional information.




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



Retrieves detailed information about a customer record, including saved payment
methods if available.

Customers can be looked up by `customerId` or `customerRef`.




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



Searches the customer database and returns matching results.

Use `query` to pass in a search string and the system will return all results whose
first or last names contain the query string.




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

#### Cash Discount



Calculates the surcharge, cash discount, and total amounts for cash transactions.

If you're using BlockChyp's cash discounting features, you can use this endpoint
to make sure the numbers and receipts for true cash transactions are consistent
with transactions processed by BlockChyp.




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
    "amount": "100.00",
    "cashDiscount": True,
    "surcharge": True,
}

# run the transaction.
response = client.cash_discount(request)

print("Response: %r" % response)


```

#### Batch History



This endpoint allows developers to query the gateway for the merchant's batch history.
The data will be returned in descending order of open date with the most recent
batch returned first.  The results will include basic information about the batch.
For more detail about a specific batch, consider using the Batch Details API.

**Limiting Results**

This API will return a maximum of 250 results.  Use the `maxResults` property to
limit maximum results even further and use the `startIndex` property to
page through results that span multiple queries.

For example, if you want the ten most recent batches, just pass in a value of
`10` for `maxResults`.  Also note that `startIndex` is zero based. Use a value of `0` to
get the first batch in the dataset.

**Filtering By Date Range**

You can also filter results by date.  Use the `startDate` and `endDate`
properties to return only those batches opened between those dates.
You can use either `startDate` and `endDate` and you can use date filters
in conjunction with `maxResults` and `startIndex`




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
    "maxResults": 250,
    "startIndex": 1,
}

# run the transaction.
response = client.batch_history(request)

print("Response: %r" % response)


```

#### Batch Details



This endpoint allows developers to pull down details for a specific batch,
including captured volume, gift card activity, expected deposit, and
captured volume broken down by terminal.

The only required request parameter is `batchId`.  Batch IDs are returned
with every transaction response and can also be discovered using the Batch
History API.




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
    "batchId": "BATCHID",
}

# run the transaction.
response = client.batch_details(request)

print("Response: %r" % response)


```

#### Transaction History



This endpoint provides a number of different methods to sift through
transaction history.

By default with no filtering properties, this endpoint will return the 250
most recent transactions.

**Limiting Results**

This API will return a maximum of 50 results in a single query.  Use the `maxResults` property
to limit maximum results even further and use the `startIndex` property to
page through results that span multiple queries.

For example, if you want the ten most recent batches, just pass in a value of
`10` for `maxResults`.  Also note that `startIndex` is zero based. Use a value of `0` to
get the first transaction in the dataset.

**Filtering By Date Range**

You can also filter results by date.  Use the `startDate` and `endDate`
properties to return only transactions run between those dates.
You can use either `startDate` or `endDate` and you can use date filters
in conjunction with `maxResults` and `startIndex`

**Filtering By Batch**

To restrict results to a single batch, pass in the `batchId` parameter.

**Filtering By Terminal**

To restrict results to those executed on a single terminal, just
pass in the terminal name.

**Combining Filters**

None of the above filters are mutually exclusive.  You can combine any of the
above properties in a single request to restrict transaction results to a
narrower set of results.




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
    "maxResults": 10,
}

# run the transaction.
response = client.transaction_history(request)

print("Response: %r" % response)


```

#### Merchant Profile



Returns detailed metadata about the merchant's configuraton, including
basic identity information, terminal settings, store and forward settings,
and bank account information for merchants that support split settlement.




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
}

# run the transaction.
response = client.merchant_profile(request)

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
