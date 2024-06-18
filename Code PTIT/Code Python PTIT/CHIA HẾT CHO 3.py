t = int(input())
for i in range(t):
    n = input()
    s = 0
    n = list(n)
    for i in n:
        s += int(i)
    if(s % 3 == 0): print("YES")
    else: print("NO")