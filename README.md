# AESandDH
Assignments that will teach you AES and Diffie-Hellman while requiring you to use advanced Python and OOP




Beginner Level
1. Understanding Symmetric Encryption: Implement a Basic XOR Cipher

    Objective: Learn the concept of symmetric encryption before moving to AES.
    Task: Implement a class XORCipher that encrypts and decrypts messages using a repeating XOR key.
    Requirements:
        Use OOP principles.
        Allow key customization.
        Implement encrypt() and decrypt() methods.

2. Implementing a Simple AES Class Using PyCryptodome

    Objective: Learn how AES works at a basic level.
    Task: Write a class AESCipher that:
        Encrypts and decrypts messages using AES in ECB mode.
        Uses a 16-byte key.
        Takes a plaintext message and returns ciphertext (and vice versa).
    Requirements:
        Use Crypto.Cipher.AES from PyCryptodome.
        Handle padding manually.

3. Implement AES in CBC Mode

    Objective: Learn about initialization vectors (IV) and why CBC mode is more secure than ECB.
    Task: Modify AESCipher to support CBC mode.
    Requirements:
        Add an IV attribute.
        Implement proper padding.
        Ensure encryption and decryption work correctly.

Intermediate Level
4. Create a Secure AES Encryption System with Key Derivation

    Objective: Learn about secure key generation using PBKDF2.
    
    Task: Modify AESCipher to derive keys from a password using PBKDF2.
    
    Requirements:
        Use Crypto.Protocol.KDF.PBKDF2 to generate a secure key.
        Allow the user to provide a password instead of a raw key.
        Store the salt with the ciphertext.

5. Implement AES-GCM with Authentication

    Objective: Learn about authenticated encryption and why it's important.
    Task: Modify AESCipher to support AES-GCM mode.
    Requirements:
        Use Crypto.Cipher.AES.MODE_GCM.
        Implement authentication tags to ensure integrity.
        Handle errors if decryption fails due to tampering.

6. Implement a Simple Diffie-Hellman Key Exchange

    Objective: Learn how two parties can securely exchange keys.
    Task: Write a class DiffieHellman that:
        Generates private and public keys.
        Exchanges public keys to generate a shared secret.
    Requirements:
        Use Python’s built-in secrets module for secure random number generation.
        Implement a method to compute the shared secret.
