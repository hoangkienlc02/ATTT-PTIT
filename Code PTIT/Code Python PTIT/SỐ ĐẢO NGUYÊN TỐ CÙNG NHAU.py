import math
for i in range(int(input())):
    s = input()
    a = ""
    for i in s:
        a = i + a
    if (math.gcd(int(s), int(a)) == 1): print("YES")
    else: print("NO")
 
