# Mã hóa bảng chữ cái
alphabet_e = {'a': '01',
            'b': '02',
            'c': '03',
            'd': '04',
            'e': '05',
            'f': '06',
            'g': '07',
            'h': '08',
            'i': '09',
            'j': '10',
            'k': '11',
            'l': '12',
            'm': '13',
            'n': '14',
            'o': '15',
            'p': '16',
            'q': '17',
            'r': '18',
            's': '19',
            't': '20',
            'u': '21',
            'v': '22',
            'w': '23',
            'x': '24',
            'y': '25',
            'z': '26',
            ' ': '32',
            '0': '48',
            '1': '49',
            '2': '50',
            '3': '51',
            '4': '52',
            '5': '53',
            '6': '54',
            '7': '55',
            '8': '56',
            '9': '57',
            'A': '65',
            'B': '66',
            'C': '67',
            'D': '68',
            'E': '69',
            'F': '70',
            'G': '71',
            'H': '72',
            'I': '73',
            'J': '74',
            'K': '75',
            'L': '76',
            'M': '77',
            'N': '78',
            'O': '79',
            'P': '80',
            'Q': '81',
            'R': '82',
            'S': '83',
            'T': '84',
            'U': '85',
            'V': '86',
            'W': '87',
            'X': '88',
            'Y': '89',
            'Z': '90',}

# Giải mã bảng chữ cái
alphabet_d = {n: c for c, n in alphabet_e.items()}

# Thuật toán Euclide: Tìm ước số chung lớn nhất của hai số
def gcd(a, b):
    if (b == 0):
        return abs(a)
    else:
        return gcd(b, a % b)


# Tạo keys, e và d
def generate_keys(p, q):

    # Public key
    n = p * q

    # Private key
    N0 = (p-1) * (q-1)

    # Public key
    # Tìm e: số nguyên tố đầu tiên nguyên tố cùng nhau tới N0
    for i in range(2, N0):
        if gcd(i, N0) == 1:
            d = i
            break
    
    # Private key
    # Tìm d: nghịch đảo nhân của e % N0
    for i in range(0, N0):
        if ((d * i) % N0) == 1:
            e = i
            break

    return n, e, d


# Mã hóa ký tự
def encrypt(char, N, e):
    return str((int(char) ** e) % N).zfill(2)


# Giải mã ký tự
def decrypt(char, N, d):
    return str((int(char) ** d) % N).zfill(2)


# Tách từ thành các ký tự
def split(word):
    return [char for char in word]


# Mã hóa đoạn tin
def encrypt_message(msg, N, e):

    # Messages
    plaintext = msg.lower().split()
    encrypted = []

    # Mã hóa đoạn tin
    for word in plaintext:

        # Tách từ thành các ký tự
        chars = split(word)

        # Tạo danh sách các ký tự được mã hóa
        encrypted_chars = [encrypt(alphabet_e[char], N, e) for char in chars]

        # Thêm từ được mã hóa vào danh sách
        encrypted_word = " ".join(encrypted_chars)
        encrypted.append(encrypted_word)

    # Ghép các từ được mã hóa với các ký tự khoảng trắng
    encrypted  = f" {encrypt(alphabet_e[' '], N, e)} ".join(encrypted)

    return encrypted


# Giải mã đoạn tin
def decrypt_message(msg, N, d):

    # Messages
    encrypted = msg.split()
    decrypted = []
    plaintext = []

    # Giải mã
    for char in encrypted:
        decrypted.append(decrypt(char, N, d))

    # Giải mã đoạn tin
    for char in decrypted:
        plaintext.append(alphabet_d[char])
    
    plaintext = "".join(plaintext)

    return plaintext

# Menu chọn
def options():
    print("Options:\n\
        0 - Tạo cặp khóa\n\
        1 - Đoạn tin cần mã hóa\n\
        2 - Đoạn tin cần giải mã\n")


# Giao diện
while True:

    # Show options
    options()

    # Nhập lựa chọn từ người dùng
    selection = input()

    # Tạo cặp khóa
    if selection == "0":

        # Chọn 2 số nguyên tố cùng nhau
        p = int(input("Nhập số nguyên tố thứ nhất: "))
        q = int(input("Nhập số nguyên tố thứ hai: "))
        print()

        try:
            # Generate values for encryption / decryption
            N, e, d = generate_keys(p, q)
            
            # Show keys
            print(f"Public key:\nN: {N}\ne: {e}\n")
            print(f"Private key:\nN: {N}\nd: {d}\n")

        except:
            print("Error: Invalid Primes\n")

    # Tạo đoạn tin cần mã hóa
    elif selection == "1":
        
        # Nhập public key
        N = int(input("Nhập public key N: "))
        e = int(input("Nhập public key e: "))
        print()

        # Nhập bản rõ
        message = input("Nhập bản rõ:\n")

        # In ra bản mã
        print(f"\nBản mã:\n{encrypt_message(message, N, e)}\n")

    # Nhập đoạn tin cần giải mã
    elif selection == "2":

        # Nhập private key
        N = int(input("Nhập private key N: "))
        d = int(input("Nhập private key d: "))
        print()

        # nhập bản mã
        message = input("Nhập bản mã:\n")

        # in ra bản rõ
        try:
            print(f"\nBản rõ:\n{decrypt_message(message, N, d)}\n")
        except:
            print("Error: Invalid Private Key\n")

    # Input validation
    else:
        print("Invalid choice\n")

    # Option to exit
    exit = input("Lựa chọn\n\
        'Y' để tiếp tục\n\
        hoặc ấn bất kỳ phím nào để thoát\n").upper()

    print()

    # Make another selection
    if exit == "Y":
        continue
    
    # Exit
    else:
        break
