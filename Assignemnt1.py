from __future__ import annotations

import random


class XORCipher:
    """
        Class the encrypts and decrypts strings using a random based key and the
        XOR between them.
    """
    def __init__(self, plaintext: str) -> None:
        self.plaintext = plaintext
        self.plaintextBin = ""
        self.key = ""
        self.plaintextBinLen = 0
        self.cipherText = ""
        self.fullKey = ""
        self.plaintextDec = ""
        self.decipheredWord = ""
        for i in plaintext:
            self.key += str(random.randrange(0, 2))

    def strToBin(self) -> None:
        """
        ::
            Converts a string into its binary representation.
        """
        self.plaintextBin = ''.join(format(ord(i), '08b') for i in self.plaintext)

    def binToStr(self) -> str:
        """
        ::
            Converts a binary string back to a readable string.

            Returns:
                (str): The deciphered word after converting the bit str and breaking to bytes.
        """
        chunksBin = [self.plaintextDec[i:i + 8] for i in range(0, len(self.plaintextDec), 8)]
        return ''.join(chr(int(i, 2)) for i in chunksBin)

    def keyFullLength(self) -> str:
        """
        ::
            Expands the key to match the length of the plaintext binary.

            Return:
                (str): The key repeated at the length of the plaintext (binary length).
        """
        return (self.key * (self.plaintextBinLen//len(self.key) + 1))[:self.plaintextBinLen]

    def encrypt(self) -> str:
        """
        ::
            Encrypts the plaintext using XOR and returns the ciphertext in binary format.

            Returns:
                (str): The ciphertext.
        """
        self.strToBin()
        self.plaintextBinLen = len(self.plaintextBin)
        self.fullKey = self.keyFullLength()
        i = 0
        while i < self.plaintextBinLen:
            self.cipherText += str(int(self.plaintextBin[i]) ^ int(self.fullKey[i]))
            i += 1
        return self.cipherText

    def decrypt(self) -> str:
        """
        ::
            Decrypts the ciphertext using XOR and returns the original plaintext.

            Returns:
                decipheredWord (str): The deciphered word.
        """
        i = 0
        while i < len(self.fullKey):
            self.plaintextDec += str(int(self.cipherText[i]) ^ int(self.fullKey[i]))
            i += 1
        self.decipheredWord = self.binToStr()
        return self.decipheredWord

    def __repr__(self):
        """
        Returns a readable representation of the encrypted and decrypted text.
        """
        print(f'Encrypted: {self.cipherText}', f'Deciphered: {self.decipheredWord}')
