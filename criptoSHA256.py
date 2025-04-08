from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, MGF1
from cryptography.hazmat.primitives.hashes import SHA256

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

symmetric_key = b"my_secret_symmetric_key"

encrypted_key = public_key.encrypt(
    symmetric_key, OAEP(mgf=MGF1(algorithm=SHA256()), algorithm=SHA256(), label=None)
)

decrypted_key = private_key.decrypt(
    encrypted_key,
    OAEP(mgf=MGF1(algorithm=SHA256()), algorithm=SHA256(), label=None)
)

print("Decrypted Key: ", decrypted_key)