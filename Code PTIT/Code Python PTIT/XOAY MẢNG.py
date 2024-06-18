t = int(input())
for i in range(t):
    n, k = map(int, input().split()) # nhập số phần tử của mảng và số k
    a = list(map(int, input().split())) # tạo mảng
    for i in range(k, n):
        print(a[i], end=" ")
    for i in range(0, k):
        print(a[i], end=" ")
    print()
    