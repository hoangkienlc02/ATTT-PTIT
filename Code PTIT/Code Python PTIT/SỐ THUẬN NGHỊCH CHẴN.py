# import math
# def check_tn(n):
#     s1 = str(n);    
#     s2 = s1[::-1];
#     if (s1 != s2): return False; 
#     return True;
# def check(n):
#     cnt = 0
#     while (n != 0):
#         s = n % 10
#         if(s % 2 != 0): return False
#         n //= 10
#         cnt +=1
#     if(cnt % 2 != 0): return False
#     return True
# t = int(input())
# for i in range(t):
#     n = int(input())
#     for i in range(22, n):
#         if(check_tn(i) and check(i)): 
#             print(i, end = " ")
#     print()

def noi(s):
    return s+s[::-1]
def ck(s):
    s = list(s)
    for i in s:
        if int(i) % 2 != 0: return False
    return True
for t in range(int(input())):
     s = input()
     cnt = int(len(s)/2)
     res = ""
     for i in range(cnt): res+="9"
     for i in range(2,int(res)):
        if ck(str(i)) and int(noi(str(i))) < int(s): print(noi(str(i)),end=" ")
     print()
    
        