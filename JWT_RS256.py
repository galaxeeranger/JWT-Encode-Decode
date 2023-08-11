import jwt
from datetime import datetime, timedelta, time
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# generate an RSA private key
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
# print("Private Key--------------->", private_key)


# serialize the private key to bytes
private_key_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)
# print("Private Key Bytes------------>",private_key_bytes)


# load the public key from the private key
public_key = private_key.public_key()
# print("Public Key--------------------->",public_key)

# serialize the public key to bytes
public_key_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

public_key_bytes1 = public_key_bytes.replace(b'\n', b'') # new public_key_bytes to check for valid Signature on jwt.io
# print("Public Key Bytes--------------->",public_key_bytes1) 


# define the payload for the JWT
payload = {
    'user_id': 101,
    'username': 'Shivmurat Gupta',
    "exp": datetime.now() + timedelta(minutes=5)
}

# encode the payload using the private key
encoded_jwt = jwt.encode(payload, private_key_bytes, algorithm='RS256')

# print("Token",encoded_jwt)

# decode the JWT using the public key
# decoded_jwt = jwt.decode(encoded_jwt, public_key_bytes, algorithms=['RS256'], options={"verify_iat": True})
# decoded_jwt = jwt.decode(encoded_jwt, public_key_bytes, algorithms=['RS256'])
# print(decoded_jwt)

try:
    decoded_jwt = jwt.decode(encoded_jwt, public_key_bytes, algorithms=['RS256'])
    print(decoded_jwt)
except Exception as e:
    print("Invalid token:", e)

