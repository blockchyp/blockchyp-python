"""
Request and response field types.
"""

# pylint: disable=too-few-public-methods

class CardType:
    """Used to differentiate credit, debit, EBT, and gift cards."""

    CREDIT = 0
    DEBIT = 1
    EBT = 2
    GIFT = 3


class SignatureFormat:
    """File formats for customer signatures."""

    NONE = "none"
    PNG = "png"
    JPG = "jpg"
    GIF = "gif"


class PromptType:
    """Specifies the type of text input for a terminal prompt."""

    AMOUNT = "amount"
    CUST_NUMBER = "customer-number"
    EMAIL = "email"
    PHONE = "phone"
    REWARDS_NUMBER = "rewards-number"
