from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def aes_encrypt(key, data):
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(data, AES.block_size))
    return iv + encrypted

def aes_decrypt(key, data):
    iv = data[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(data[16:]), AES.block_size)
    return decrypted

key = b'hoangtrungkien02'
data = b'Hello, I am B20DCAT098'

encrypted = aes_encrypt(key, data)
print(f"Encrypted data: {encrypted}")

decrypted = aes_decrypt(key, encrypted)
print(f"Decrypted data: {decrypted}")