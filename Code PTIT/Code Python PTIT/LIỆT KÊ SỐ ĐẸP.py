def ck(s):
    for i in s:
        if i!='0' and i!='2' and i!='4' and i!='6' and i!='8': return False
    return True
def dup(n):
    s = str(n)
    s1 = s[::-1];
    return s+s1
for t in range(int(input())):
    s = input()
    n = int(len(s)/2)
    m =""
    for i in range(n): m+='9'
    for i in range(1,int(m)):
        if ck(str(i)) and int(dup(i)) < int(s): print(dup(i),end=" ")
    print()
    