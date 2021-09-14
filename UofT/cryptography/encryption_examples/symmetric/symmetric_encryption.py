from cryptography.fernet import Fernet

key_path = "symmetric_key.txt"
key_file = open(key_path, "rb")
key = key_file.read()

cipher = Fernet(key)

message = b"Hello everyone. My name is Samuel Atkins."

encrypted_text = cipher.encrypt(message)

print(encrypted_text)

decrypted_text = cipher.decrypt(encrypted_text)

print(decrypted_text)