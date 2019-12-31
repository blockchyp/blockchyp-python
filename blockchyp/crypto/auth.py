import hashlib
import hmac
import os

from blockchyp.util import iso_timestamp


NONCE_SIZE = 32
HEADER_NONCE = "Nonce"
HEADER_TIMESTAMP = "Timestamp"
HEADER_AUTHORIZATION = "Dual"


def auth_headers(api_key, bearer_token, signing_key):
    # type: (str, str, str) -> dict
    """Generates dual authentication headers for a request."""

    nonce = os.urandom(NONCE_SIZE).hex()
    timestamp = iso_timestamp()

    payload = bytes(f"{api_key}{bearer_token}{timestamp}{nonce}", "utf-8")
    key = bytes.fromhex(signing_key)

    signature = hmac.new(key, payload, digestmod=hashlib.sha256).digest().hex()

    auth = f"Dual {bearer_token}:{api_key}:{signature}"

    return {
        "Nonce": nonce,
        "Timestamp": timestamp,
        "Authorization": auth,
    }
