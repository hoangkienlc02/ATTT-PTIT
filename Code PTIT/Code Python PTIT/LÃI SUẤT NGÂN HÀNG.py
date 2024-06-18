import math
for i in range(int(input())):
    n, x, m = map(float, input().split())
    x /= 100
    s = math.log(m / n, 1 + x)
    # ép kiểu s từ float -> int rồi cộng thêm 1
    a = int(s)
    a = a + 1
    print(int(a))
    
        
# m = n.(1+x/s)^t
# m/n = (1 + x/s)^t
# log(m/n) = log(1+x/s)^t
# log(m/n) = (t)log(1+x), công thức: (log(b,a)=log(b)/log(a))
# t = log(m/n, 1+x)