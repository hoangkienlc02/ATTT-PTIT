import timeit
import hashlib
from passlib.hash import argon2
import bcrypt
import os

password = b'password123'

# Argon2
argon = argon2.using(
    salt_len=12, # độ dài của muối
    time_cost=2, # số lần lặp
    memory_cost=1000, # bộ nhớ cần thiết
    parallelism=2, # số luồng thực hiện
    hash_len=32, # độ dài chuỗi đầu ra
)
argon_time = timeit.timeit(lambda: argon.hash(password), number=1000) * 1000
argon_hash = argon.hash(password)
argon_memory = len(argon_hash.encode('utf-8'))

# Bcrypt
bcrypt_time = timeit.timeit(lambda: bcrypt.hashpw(password, bcrypt.gensalt()), number=1000)
bcrypt_hash = bcrypt.hashpw(password, bcrypt.gensalt())
bcrypt_memory = len(bcrypt_hash)

# SHA256
#Tạo một chuỗi muối ngẫu nhiên bằng cách sử dụng os.urandom()
salt = os.urandom(16) #Lấy độ dài của muối là 16 bytes, có thể chỉnh tùy ý
salted_password = salt + password

sha256_time = timeit.timeit(lambda: hashlib.sha256(salted_password).hexdigest(), number=1000) * 1000
sha256_hash = hashlib.sha256(salted_password).hexdigest()
sha256_memory = len(sha256_hash)

# Print results
print('Argon2 hash: ' + argon_hash)
print('Thời gian: {time} milliseconds'.format(time=argon_time))
print('Bộ nhớ: {memory} bytes'.format(memory=argon_memory))
print()

print('Bcrypt hash: ', end='')
print(bcrypt_hash)
print('Thời gian: {time} milliseconds'.format(time=bcrypt_time))
print('Bộ nhớ: {memory} bytes'.format(memory=bcrypt_memory))
print()

print('SHA256 hash: ' + sha256_hash)
print('Thời gian: {time} milliseconds'.format(time=sha256_time))
print('Bộ nhớ: {memory} bytes'.format(memory=sha256_memory))