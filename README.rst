BlockChyp Python SDK
====================

The official library for accessing the BlockChyp Terminal and Gateway APIs
from Python.


Install
-------

BlockChyp can be simply installed by running::

    pip install blockchyp


Documentation
-------------

Full documentation can be found on the `BlockChyp SDK Developers Guide`_.


Transaction Code Examples
-------------------------

You don't want to read words. You want examples. Here's a quick rundown of the
stuff you can do with the BlockChyp Python SDK and a few basic examples.


Charge
^^^^^^

Executes a standard direct preauth and capture.

.. code-block:: python

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


Preauthorization
^^^^^^^^^^^^^^^^

Executes a preauthorization intended to be captured later.

.. code-block:: python

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


Terminal Ping
^^^^^^^^^^^^^

Tests connectivity with a payment terminal.

.. code-block:: python

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


Balance
^^^^^^^

Checks the remaining balance on a payment method.

.. code-block:: python

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


Terminal Clear
^^^^^^^^^^^^^^

Clears the line item display and any in progress transaction.

.. code-block:: python

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


Terms & Conditions Capture
^^^^^^^^^^^^^^^^^^^^^^^^^^

Prompts the user to accept terms and conditions.

.. code-block:: python

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


Update Transaction Display
^^^^^^^^^^^^^^^^^^^^^^^^^^

Appends items to an existing transaction display Subtotal, Tax, and Total are
overwritten by the request. Items with the same description are combined into
groups.

.. code-block:: python

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


New Transaction Display
^^^^^^^^^^^^^^^^^^^^^^^

Displays a new transaction on the terminal.

.. code-block:: python

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


Text Prompt
^^^^^^^^^^^

Asks the consumer text based question.

.. code-block:: python

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


Boolean Prompt
^^^^^^^^^^^^^^

Asks the consumer a yes/no question.

.. code-block:: python

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


Display Message
^^^^^^^^^^^^^^^

Displays a short message on the terminal.

.. code-block:: python

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


Refund
^^^^^^

Executes a refund.

.. code-block:: python

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


Enroll
^^^^^^

Adds a new payment method to the token vault.

.. code-block:: python

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


Gift Card Activation
^^^^^^^^^^^^^^^^^^^^

Activates or recharges a gift card.

.. code-block:: python

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


Time Out Reversal
^^^^^^^^^^^^^^^^^

Executes a manual time out reversal.

We love time out reversals. Don't be afraid to use them whenever a request to a
BlockChyp terminal times out. You have up to two minutes to reverse any
transaction. The only caveat is that you must assign transactionRef values when
you build the original request. Otherwise, we have no real way of knowing which
transaction you're trying to reverse because we may not have assigned it an id
yet. And if we did assign it an id, you wouldn't know what it is because your
request to the terminal timed out before you got a response.

.. code-block:: python

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


Capture Preauthorization
^^^^^^^^^^^^^^^^^^^^^^^^

Captures a preauthorization.

.. code-block:: python

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


Close Batch
^^^^^^^^^^^

Closes the current credit card batch.

.. code-block:: python

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


Void Transaction
^^^^^^^^^^^^^^^^

Discards a previous preauth transaction.

.. code-block:: python

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


License
-------

Copyright BlockChyp, Inc., 2019.

Distributed under the terms of the `MIT`_ license, blockchyp-python is free and open source software.

.. _`BlockChyp SDK Developers Guide`: https://docs.blockchyp.com/sdk-guide/index.html
.. _`MIT`: https://github.com/blockchyp/blockchyp-python/blob/master/LICENSE
