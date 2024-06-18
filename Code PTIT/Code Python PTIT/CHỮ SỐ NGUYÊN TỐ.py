import math
def check_nt(n):
    if (n < 2): return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n % i == 0): return False
    return True
def check (n):
    if (check_nt(len(n)) == False): return False
    demNT = 0
    dem = 0
    for i in n:
        if check_nt(int(i)): demNT+=1
        else: dem+=1
    if (demNT < dem): return False
    return True
t = int(input())
for i in range(t):
    n = input()
    if(check(n) == True): print("YES")
    else: print("NO")
            

