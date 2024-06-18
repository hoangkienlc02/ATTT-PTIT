def check(n):
    for i in range(1, len(n)):
        if (n[i] < n[i-1]): return False
    return True
t = int(input())
for i in range(t):
    s = input()
    if (check(s)): 
        print("YES")
    else: print("NO")