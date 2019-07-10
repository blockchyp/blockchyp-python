"""
This file defines the BlockChyp Cryptography Services
"""


# from datetime import datetime


GROUP_14_PRIME = ("FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22"
                  "514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6"
                  "F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3D"
                  "C2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB"
                  "9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E8603"
                  "9B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA0510"
                  "15728E5A8AACAA68FFFFFFFFFFFFFFFF")
GROUP_14_GENERATOR = 2

class CryptoUtils:
    """
    Provides encryption and associated services for the BlockChyp Client
    """
    def generate_gateway_headers(self, creds):
        """
        Generates headers to be used in aquiring gateway configuration
        """

    def encrypt(self, hex_key, plain_text):
        """
        Encrypts a block of text
        """

    def sha_256_hash(self, msg):
        """
        Generates a SHA hash
        """

    def validate_signature(self, public_key, msg, sig):
        """
        Validates a digital signature
        """

    def decrypt(self, hex_key, cipher_text):
        """
        Decrypts a block of encrypted text
        """

    def generate_diffie_hellman_keys(self):
        """
        Generates a new set of Diffe Hellman Keys
        """

    def compute_shared_key(self, private_key, other_public_key):
        """
        Computes a shared key based on a private key and a public key
        """

    @staticmethod
    def generate_nonce():
        """
        Generates a new nonce
        """

    @staticmethod
    def generate_iso_timestamp():
        """
        Generates a timestamp based on the current time in UTC
        """
