def check(n):
    sum = 0
    for i in n:
        sum += int(i)
    if(sum == int(str(sum)[::-1]) and sum > 10): return True  
    # int(str(sum)[::-1]) là chuyển sum về string sau đó đảo ngược xâu sum rồi chuyển về int
    return False
t = int(input())
for i in range(t):
    s = input()
    if(check(s)): print("YES")
    else: print("NO")
    
