import base64
import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

from blockchyp.error import BlockChypError


IV_LENGTH = 16
BLOCK_SIZE = 128


def encrypt(plaintext, key):
    """Encrypts the string payload to base64 encoded ciphertext."""
    iv = os.urandom(IV_LENGTH)

    encryptor = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
        backend=default_backend(),
    ).encryptor()

    padder = padding.PKCS7(BLOCK_SIZE).padder()

    payload = padder.update(bytes(plaintext, "utf-8")) + padder.finalize()

    ciphertext = encryptor.update(payload) + encryptor.finalize()

    return base64.b64encode(iv + ciphertext).decode("utf-8")


def decrypt(ciphertext, key):
    """Decrypts base64 encoded ciphertext to a plaintext string."""
    raw = base64.b64decode(ciphertext)

    if len(raw) < IV_LENGTH:
        raise BlockChypError("Payload too short.")

    iv = raw[:IV_LENGTH]
    payload = raw[IV_LENGTH:]

    decryptor = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
        backend=default_backend(),
    ).decryptor()

    unpadder = padding.PKCS7(BLOCK_SIZE).unpadder()

    plaintext = decryptor.update(payload) + decryptor.finalize()

    unpadded = unpadder.update(plaintext) + unpadder.finalize()

    return unpadded.decode("utf-8")
