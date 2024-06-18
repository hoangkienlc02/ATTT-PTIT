from hashlib import sha256
from passlib.hash import argon2
from os import urandom 
from base64 import b64encode 
from time import time
import bcrypt

#Bcrypt
# b'' là encode
# password1 = b'HoangTrungKienAT098_lc02'
# start = time()
# _bcrypt_hash = bcrypt.hashpw(password1, bcrypt.gensalt())
# end = time()
# print('Bcrypt take {diff} miniseconds' .format(diff=(end - start)))
# print("Chuỗi băm: " , end='')
# print(_bcrypt_hash)
# print()



password = 'HoangTrungKienAT098_lc02!@#$$'
#SHA256  
def salted_sha256(massage):
    salt = b64encode(urandom(16))
    _hash = b64encode(
        sha256(massage + salt)\
            .digest()
    ).decode()
    return salt.decode() + '$' + _hash

start = time()
_sha_hash = salted_sha256(password.encode())
end = time()
print('SHA256 take {diff} miniseconds' .format(diff=(end - start)*1000))
print("Chuỗi băm: " +_sha_hash)
print()


#ARGON2
_argon = argon2.using(
    salt_len=16,
    digest_size=32,
    parallelism=2,
    rounds=2,
    memory_cost=1000, 
)
start = time()
_hash = _argon.hash(password)
end = time()
print('ARGON2 take {diff} miniseconds' .format(diff=(end - start)*1000))
print("Chuỗi băm: " +_hash)
# print(_argon.verify(key, _hash))
# print(len(_hash.split('$')[-1]))