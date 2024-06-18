a, k, n = map(int, input().split())
b = k - a % k
if (a + b > n): print("-1")
else:
    for i in range(b, n - a + 1, k):
        print(i, end=" ")
