from __future__ import annotations

import base64

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class AESCipher:
    """
        A class for encrypting and decrypting messages using AES in ECB mode.
        This class supports PKCS7 padding and Base64 encoding for the ciphertext.
    """
    def __init__(self, key: str):
        """
        Accepts a key (string) and pads it if necessary to be 16, 24, or 32 bytes (AES key sizes).
        """
        self.blockSize = 16
        self.key = pad(key.encode("utf-8"), self.blockSize)

    def encrypt(self, plaintext: str) -> str:
        """
        ::
            Encrypts the plaintext using  AES in ECB mode and returns the ciphertext in binary format.

            Parameters:
                plaintext (str): Data being encrypted.

            Returns:
                (str)          : Applied PKCS7 padding and encoded the AES-encrypted data in Base64 for readability.
        """
        cipher = AES.new(self.key, AES.MODE_ECB)
        paddedText = pad(plaintext.encode(), self.blockSize)
        return base64.b64encode(cipher.encrypt(paddedText)).decode()

    def decrypt(self, ciphertext: str) -> str:
        """
        ::
            Decrypts the ciphertext and returns the original plaintext.

            Parameters:
                ciphertext (str): Data being decrypted.

            Returns:
                (str)           : Decrypts the base64-encoded ciphertext back to plaintext.

        """
        cipher = AES.new(self.key, AES.MODE_ECB)
        encryptedBytes = base64.b64decode(ciphertext)
        return unpad(cipher.decrypt(encryptedBytes), self.blockSize).decode()
