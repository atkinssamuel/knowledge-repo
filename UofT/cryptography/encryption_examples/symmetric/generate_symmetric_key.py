from cryptography.fernet import Fernet

key = Fernet.generate_key()

key_path = "symmetric_key.txt"

key_file = open(key_path, "wb")
key_file.write(key)
key_file.close()
