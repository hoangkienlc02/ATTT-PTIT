import math
def nto(n) :
    if (n < 2) : return False
    for i in range(2, int(math.sqrt(n)) + 1) :
        if (n % i == 0) : return False
    return True
def check(n):
    k = 0
    sum = 0
    a = n
    while(n != 0):
        i = n % 10
        if(nto(i) != True): return False
        k = k * 10 + i
        sum += i
        n //= 10
    if(nto(a) and nto(sum) and nto(k)): return True
    return False
t = int(input())
for i in range(t):
    n = int(input())
    if(check(n) == True): print("Yes")
    else: print("No") 

