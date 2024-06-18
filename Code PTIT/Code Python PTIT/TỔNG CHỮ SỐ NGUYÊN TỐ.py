import math
def check_nt(n):
    if (n < 2): return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0): return False
    return True
for i in range(int(input())):
    n = int(input())
    sum = 0
    while (n != 0):
        sum = sum + (n % 10)
        n //= 10
    if (check_nt(sum)): print("YES")
    else: print("NO")
