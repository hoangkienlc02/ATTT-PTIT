def check(n):
    for i in range(2, len(n)):
        if (n[i] != n[i-2]): return False
    return True
t= int(input())
for i in range(t):
    n = input()
    if(check(n) == True): print("YES")
    else: print("NO")