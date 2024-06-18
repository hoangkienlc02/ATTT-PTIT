import math
def check(a, b):
    if math.gcd(a, b) == 1 : return True
    return False
a, b = map(int, input().split())
b += 1
for i in range(a, b):
    for j in range(i + 1, b):
        for k in range(j + 1, b):
            if (check(i, j) == True and check(i, k) == True and check(j, k) == True):
                print("(",end = "")
                print(i, end = ", ")
                print(j, end = ", ")
                print(k, end = ")\n")