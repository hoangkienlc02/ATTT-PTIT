import math
def nto(n):
    if(n < 2): return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n % i == 0): return False
    return True
def check(n):
    s = 0
    for i in range(len(n)):
        if (i % 2) != (int(n[i]) % 2): return False # kiểm tra vị trí chẵn có là chữ số chẵn không
        s += int(n[i])
    if(nto(s) != True): return False 
    return True
t = int(input())
for i in range(t):
    s = input()
    if(check(s) == True): print("YES")
    else: print("NO")