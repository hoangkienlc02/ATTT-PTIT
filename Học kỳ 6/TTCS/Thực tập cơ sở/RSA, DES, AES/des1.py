from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def des_encrypt(key, data):
    iv = get_random_bytes(8)
    cipher = DES.new(key, DES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(data, DES.block_size))
    return iv + encrypted

def des_decrypt(key, data):
    iv = data[:8]
    cipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(data[8:]), DES.block_size)
    return decrypted

key = b'kienat098'
data = b'Hello, I am B20DCAT098'

encrypted = des_encrypt(key, data)
print(f"Encrypted data: {encrypted}")

decrypted = des_decrypt(key, encrypted)
print(f"Decrypted data: {decrypted}")