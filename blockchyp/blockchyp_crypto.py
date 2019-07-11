"""
This file defines the BlockChyp Cryptography Services
"""


from datetime import datetime
import base64
import hashlib
import hmac
import os


class CryptoUtils:
    """
    Provides encryption and associated services for the BlockChyp Client
    """
    def generate_gateway_headers(self, creds):
        """
        Generates headers to be used in aquiring gateway configuration
        """
        nonce = self.generate_nonce()
        time_stamp = self.generate_iso_timestamp()
        to_sign = (creds["api_key"] + creds["bearer_token"] + time_stamp + nonce).encode("UTF-8")

        key = bytearray.fromhex(creds["signing_key"])
        sig = hmac.new(key, to_sign, hashlib.sha256).hexdigest()
        results = {
            "nonce": nonce,
            "timestamp": time_stamp,
            "auth_header": "Dual " + creds["bearer_token"] + ":" + creds["api_key"] + ":" + sig,
        }

        return results

    @staticmethod
    def generate_nonce():
        """
        Generates a new nonce
        """
        rand = base64.b32encode(os.urandom(32)).strip(b"=").decode("UTF-8")

        return rand

    @staticmethod
    def generate_iso_timestamp():
        """
        Generates a timestamp based on the current time in UTC
        """
        time = datetime.utcnow().isoformat('T', "seconds") + 'Z'

        return time
