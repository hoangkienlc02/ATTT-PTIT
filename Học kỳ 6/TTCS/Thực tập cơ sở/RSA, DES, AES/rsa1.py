from math import gcd

def rsa_generate_key_pair(p, q):
    # Step 1: Compute n = p * q and phi(n) = (p - 1) * (q - 1)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Step 2: Choose an integer e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
    e = 65537  # Commonly used value for e
    while gcd(e, phi_n) != 1:
        e += 2

    # Step 3: Compute the modular inverse d of e modulo phi(n)
    d = pow(e, -1, phi_n)

    # Return the public key (n, e) and the private key (n, d)
    return (n, e), (n, d)

def rsa_encrypt(public_key, plaintext):
    # Extract the public key components n and e
    n, e = public_key

    # Convert the plaintext to an integer m
    m = int.from_bytes(plaintext, 'big')

    # Compute the ciphertext c = m^e mod n
    c = pow(m, e, n)

    # Convert the ciphertext to bytes and return it
    ciphertext = c.to_bytes((c.bit_length() + 7) // 8, 'big')
    print(f"Encrypted data: {ciphertext}")
    return ciphertext

def rsa_decrypt(private_key, ciphertext):
    # Extract the private key components n and d
    n, d = private_key

    # Convert the ciphertext to an integer c
    c = int.from_bytes(ciphertext, 'big')

    # Compute the plaintext m = c^d mod n
    m = pow(c, d, n)

    # Convert the plaintext to bytes and return it
    plaintext = m.to_bytes((m.bit_length() + 7) // 8, 'big')
    print(f"Decrypted data: {plaintext}")
    return plaintext

# Choose two large prime numbers p and q
p = 13
q = 17

# Generate key pair
public_key, private_key = rsa_generate_key_pair(p, q)

# Encrypt data
plaintext = b'This is a secret message.'
ciphertext = rsa_encrypt(public_key, plaintext)

# Decrypt data
decryptedtext = rsa_decrypt(private_key, ciphertext)