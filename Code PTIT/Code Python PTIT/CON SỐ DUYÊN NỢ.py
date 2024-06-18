t = int(input())
for i in range(t):
    n = input()
    for i in n:
        if(n[0] == n[-1]): print("YES")
        else: print("NO")
        break