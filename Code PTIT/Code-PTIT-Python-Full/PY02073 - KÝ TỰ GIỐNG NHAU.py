# Lazygarde
    
class Data :
    def __init__(self, x, y):
        self.x = x
        self.y = y

t = int(input())
for z in range(t):
    n = int(input())
    a, q = [-1] * 110, []
    x, y, z = [int(i) for i in input().split()]
    q.append(Data(0, 0))
    a[0] = 0
    while len(q) > 0 :
        u = q[-1]
        q.pop()
        if u.x + 1 < 110 and (a[u.x + 1] == -1 or a[u.x + 1] > u.y + x) :
            a[u.x + 1] = a[u.x] + x
            q.append(Data(u.x + 1, u.y + x))
        if u.x - 1 > 0 and (a[u.x - 1] == -1 or a[u.x - 1] > u.y + y) :
            a[u.x - 1] = a[u.x] + y
            q.append(Data(u.x - 1, u.y + y))
        if u.x * 2 < 110 and (a[u.x * 2] == -1 or a[u.x * 2] > u.y + z) :
            a[u.x * 2] = a[u.x] + z
            q.append(Data(u.x * 2, u.y + z))
        
    print(a[n])

