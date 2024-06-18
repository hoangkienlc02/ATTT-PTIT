import math
def check_nt(n):
    if (n < 2): return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0): return False
    return True
for i in range(int(input())):
    a, b = map(int, input().split())
    n = math.gcd(a, b)
    s = 0
    while(n != 0):
        s = s + (n % 10)
        n //= 10
    if (check_nt(s)): print("YES")
    else: print("NO")
