from cryptography.hazmat.primitives import hashes
from Crypto.Hash import MD5
import hashlib

print('pyCrypto MD5')
h = MD5.new()
h.update(password)
print(h.hexdigest())
