import math
def nto(n):
    if(n < 2): return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n % i == 0): return False
    return True
def check(n):
    dem = 0
    demNt = 0
    cnt = 0
    while(n != 0):
        s = n % 10
        if(nto(s)): demNt += 1
        else: dem +=1
        n //= 10
        cnt += 1
    if(nto(cnt) == True and demNt > dem): return True
    return False 
t = int(input())
for i in range(t):
    s = int(input())
    if(check(s) == True): print("YES")
    else: print("NO") 