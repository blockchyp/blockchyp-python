import os

from blockchyp import crypto


def test_auth_headers():
    """Assert that auth headers are encoded."""

    result = crypto.auth_headers(
        "SGLATIFZD7PIMLAQJ2744MOEGI",
        "FI2SWNNJHJVO6DBZEF26YEHHMY",
        "c3a8214c318dd470b0107d6c111f086b60ad695aaeb598bf7d1032eee95339a0",
    )

    for key, value in result.items():
        print(f"{key}: {value}")

    assert len(result) == 3
    assert result.get("Nonce")
    assert result.get("Timestamp")
    assert result.get("Authorization")


def test_round_trip():
    """Assert that messages are unchanged by encrypting and decrypting."""

    for _ in range(1000):
        msg = os.urandom(100).hex()
        key = os.urandom(32)

        ciphertext = crypto.encrypt(msg, key)

        plaintext = crypto.decrypt(ciphertext, key)

        assert plaintext == msg


def test_encoding():
    """Assert that encrypted and decrypted messages are UTF-8 strings."""
    msg = "We drift through the heavens 果てない想い"
    key = os.urandom(32)

    ciphertext = crypto.encrypt(msg, key)

    assert isinstance(ciphertext, str)

    plaintext = crypto.decrypt(ciphertext, key)

    assert isinstance(plaintext, str)
