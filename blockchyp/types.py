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
    FIRST_NAME = "first-name"
    LAST_NAME = "last-name"


class AVSResponse:
    """Contains address verification results."""

    NOT_APPLICABLE = ""
    NOT_SUPPORTED = "not_supported"
    RETRY = "retry"
    NO_MATCH = "no_match"
    ADDRESS_MATCH = "address_match"
    POSTAL_CODE_MATCH = "zip_match"
    ADDRESS_AND_POSTAL_CODE_MATCH = "match"

class CVMType:
    """Contains customer verification methods."""

    SIGNATURE = "Signature"
    OFFLINE_PIN = "Offline PIN"
    ONLINE_PIN = "Online PIN"
    CDCVM = "CDCVM"
    NO_CVM = "No CVM"
