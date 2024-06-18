def check(n):
    a = int(n)
    s = 0
    while(a != 0):
        s += a % 10
        a //= 10
    if (s % 10 != 0): return False
    for i in range(1, len(n)):
        if (abs(int(n[i]) - int(n[i-1])) != 2): return False
    return True
t = int(input())
for i in range(t):
    n = input()
    if(check(n) == True): print("YES")
    else: print("NO")
