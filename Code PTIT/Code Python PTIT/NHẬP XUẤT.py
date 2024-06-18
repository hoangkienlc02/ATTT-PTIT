"""#s = input('Xin nhap chuoi ki tu bat ky: ')
#print(s)
# Nhập các số trên cùng 1 dòng
# Bước 1: Nhập
s = input('Nhap 3 so: ')
# Bước 2: Tách các số ra
a = s.split() 
# Bước 3: Sử dụng hàm map để ép các phần tử trong list => kiểu dữ liệu mong muốn
x, y, z = map(int, a)
print(x + y + z)"""
# Ví dụ khác:
n, m, b, c = map(int, input('Nhap 4 so: ').split())
print(n, m, b, c)
print(n + m + b + c)