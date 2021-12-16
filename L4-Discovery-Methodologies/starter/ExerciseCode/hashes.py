from cryptography.hazmat.primitives import hashes
from Crypto.Hash import MD5
import hashlib

def generateString():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(8))
    return result_str

#This is just to setup a init password for the account, and then is replace witht the user actual password.
password = generateString()
print(password)

#We need to hash the passwords, so we dont store it in cleartext
print('MD5')
hashpassword = hashlib.md5(password)
print(hashpassword)

#We need to hash the passwords, so we dont store it in cleartext
print('pyCrypto MD5')
h = MD5.new()
h.update(password)
print(h.hexdigest())
