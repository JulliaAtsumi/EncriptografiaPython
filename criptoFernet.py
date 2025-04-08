from cryptography.fernet import Fernet
key = Fernet.generate_key()
fernet = Fernet(key)
message = "Hello World"
encrypted_message = fernet.encrypt(message.encode())
decrypted_message = fernet.decrypt(encrypted_message).decode()
print("Encrypted: ", encrypted_message)
print("Decrypted: ", decrypted_message)