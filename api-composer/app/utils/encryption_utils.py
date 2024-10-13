from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os
import json
import base64

SECRET_KEY = base64.b64decode(os.getenv("ENCRYPTION_SECRET_KEY"))
IV = base64.b64decode(os.getenv("ENCRYPTION_IV"))


def encrypt_data(data: dict) -> str:
    """Encrypt data using AES-CBC with PKCS7 padding."""
    try:
        plaintext = json.dumps(data).encode()

        # Pad the plaintext to a multiple of 16 bytes
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plaintext) + padder.finalize()

        # Encrypt using AES-CBC mode
        cipher = Cipher(algorithms.AES(SECRET_KEY), modes.CBC(IV))
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

        # Return encrypted data as a Base64-encoded string
        return base64.b64encode(encrypted_data).decode('utf-8')

    except Exception as e:
        print(f"Encryption Error: {e}")
        raise


def decrypt_data(encrypted_data: str) -> dict:
    """Decrypt data encrypted with AES-CBC and return the original dictionary."""
    try:
        encrypted_bytes = base64.b64decode(encrypted_data)

        # Decrypt using AES-CBC mode
        cipher = Cipher(algorithms.AES(SECRET_KEY), modes.CBC(IV))
        decryptor = cipher.decryptor()
        decrypted_padded_data = decryptor.update(
            encrypted_bytes) + decryptor.finalize()

        # Remove padding from the decrypted data
        unpadder = padding.PKCS7(128).unpadder()
        decrypted_data = unpadder.update(
            decrypted_padded_data) + unpadder.finalize()

        return json.loads(decrypted_data.decode('utf-8'))

    except Exception as e:
        print(f"Decryption Error: {e}")
        raise
