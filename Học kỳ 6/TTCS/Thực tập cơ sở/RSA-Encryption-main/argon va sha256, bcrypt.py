import time
import timeit
import hashlib
import argon2
from hashlib import sha256
from passlib.hash import argon2
from os import urandom 
from base64 import b64encode 
import bcrypt
import os
import base64

password = b'password123'

# Argon2
_argon = argon2.using(
    salt_len=12, # độ dài của muối
    time_cost=2, # số lần lặp
    memory_cost=1000, # bộ nhớ cần thiết
    parallelism=2, # số luồng thực hiện
    hash_len=32, # độ dài chuỗi đầu ra
)
start = timeit.default_timer()
_argon_hash = _argon.hash(password)
end = timeit.default_timer()
argon2_time = (end - start) * 1000
argon2_memory = len(_argon_hash) 

# Bcrypt
start = timeit.default_timer()
_bcrypt_hash = bcrypt.hashpw(password, bcrypt.gensalt()) #gensalt(): muối mặc định là 12 và có thể chỉnh độ dài của muối tùy ý "gensalt(16)"
end = timeit.default_timer()
bcrypt_time = (end - start)
bcrypt_memory = len(_bcrypt_hash) 

# SHA256
#Tạo một chuỗi muối ngẫu nhiên bằng cách sử dụng os.urandom()
salt = os.urandom(16) #Lấy độ dài của muối là 16 bytes, có thể chỉnh tùy ý
salt_encoded = base64.b64encode(salt)
salted_password = salt + password

start = timeit.default_timer()
_sha256_hash = hashlib.sha256(salted_password).hexdigest()
end = timeit.default_timer()
sha256_time = (end - start) * 1000
sha256_memory = len(_sha256_hash)


# Print results
print('Argon2: ' + _argon_hash)
print('Thời gian: {time} milliseconds'.format(time=argon2_time))
print('Bộ nhớ: {memory} bytes'.format(memory=argon2_memory))
print()

print('Bcrypt: ', end='')
print(_bcrypt_hash)
print('Thời gian: {time} milliseconds'.format(time=bcrypt_time))
print('Bộ nhớ: {memory} bytes'.format(memory=bcrypt_memory))
print()

print('SHA256: ' + _sha256_hash)
print('Thời gian: {time} milliseconds'.format(time=sha256_time))
print('Bộ nhớ: {memory} bytes'.format(memory=sha256_memory))


