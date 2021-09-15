from cryptography.fernet import Fernet

"""
This file generates 4 keys: Alice_pub.txt, Alice_priv.txt, Bob_pub.txt, Bob_priv.txt corresponding to the public and
private keys for both Alice and Bob
"""

key_files = ["Alice_pub.txt", "Alice_priv.txt", "Bob_pub.txt", "Bob_priv.txt"]
for key_file_str in key_files:
    key_file = open("keys/" + key_file_str, "wb")
    key_file.write(Fernet.generate_key())
    key_file.close()
