#HOÀNG TRUNG KIÊN-B20DCAT098

from Crypto.Cipher import AES
from secrets import token_bytes

key = token_bytes(16) #Độ dài của key là 16 byte

#Hàm mã hóa
def encrypt(msg):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag

#Hàm giải mã
def decrypt(nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False

nonce, ciphertext, tag = encrypt(input('Nhập bản rõ: '))
print(f'Bản mã: {ciphertext}')
plaintext = decrypt(nonce, ciphertext, tag)

if not plaintext:
    print('Tin nhắn bị hỏng!')
else:
    input('Nhập bản mã: ')
    print(f'Bản mã đã được giải mã: {plaintext}')