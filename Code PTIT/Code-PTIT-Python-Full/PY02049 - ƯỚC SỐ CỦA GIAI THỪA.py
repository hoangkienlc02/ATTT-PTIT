t = int(input())
for i in range(t) :
    n, p = [int(x) for x in input().split()]
    d = 0
    for i in range(2, n + 1) :
        while i % p == 0 :
            i /= p
            d += 1
    print(d)

