from cryptography.fernet import Fernet

"""
Fernet encrypts and decrypts using AES in CBC mode with a 128-bit key for encryption using PKCS7 padding. For 
authentication, it uses HMAC and SHA256. The initialization vectors are generated using os.urandom().
"""

key_path = "symmetric_key.txt"
key_file = open(key_path, "rb")
key = key_file.read()

cipher = Fernet(key)

message = b"Hello everyone. My name is Samuel Atkins."

encrypted_text = cipher.encrypt(message)

print(encrypted_text)

decrypted_text = cipher.decrypt(encrypted_text)

print(decrypted_text)