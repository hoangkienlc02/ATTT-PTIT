def check(p) :
    for i in a:
        if int(i / p) == int(i / (p + 1)) :
            return 0
    return 1
n = int(input())
a = [int(x) for x in input().split()]
s, ans = min(a), 0
for i in range(s, 0, -1) :
    if check(i) :
        for j in range(n) :
            ans += int(a[j] / (i + 1)) + 1
        break
print(ans)
