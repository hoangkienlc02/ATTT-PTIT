t = int(input())
for i in range(t):
    n = int(input())
    sum = 0
    k = 1
    if (n % 2 == 0): 
        k = 2
    for i in range(k, n + 1, 2):
        sum += 1/i
    print("{:.6f}".format(sum))


