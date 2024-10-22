
    
from datetime import datetime

tg = [0, 25, 34, 50, 80]

class KhachHang :
    def __init__(self, id, ten, phong, ngayDen, ngayDi, phuThu) :
        self.id = 'KH{0:0>2}'.format(id)
        self.ten = ten
        self.phong = phong
        self.ngayO = str(datetime.strptime(ngayDi, '%d/%m/%Y') - datetime.strptime(ngayDen, '%d/%m/%Y')).split()[0]
        if self.ngayO == '0:00:00' : self.ngayO = 1
        else : self.ngayO = int(self.ngayO) + 1
        self.tong = tg[int(self.phong[0])] * self.ngayO + phuThu
    
    def __str__(self):
        return self.id + ' ' + self.ten + ' ' + self.phong + ' ' + str(self.ngayO) + ' ' + str(self.tong)

n = int(input())
a = []
for i in range(n):
    a.append(KhachHang(i+1, input(), input(), input().strip(), input().strip(), int(input())))
a.sort(key = lambda k : -k.tong)
print(*a, sep = '\n')

