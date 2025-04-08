import rsa
public_key, private_key = rsa.newkeys(512)
message = "Hello World".encode()
encrypted_message = rsa.encrypt(message, public_key)
decrypted_message = rsa.decrypt(encrypted_message, private_key).decode()
print("Encrypted: ", encrypted_message)
print("Decrypted: ", decrypted_message)