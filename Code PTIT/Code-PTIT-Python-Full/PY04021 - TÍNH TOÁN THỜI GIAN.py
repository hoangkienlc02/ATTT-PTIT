# Lazygarde

class Gamer :
    thoiGian = 0
    def __init__(self, ma, ten, gioVao, gioRa) :
        self.ma = ma
        self.ten = ten
        self.thoiGian = gioRa[0] * 60 + gioRa[1] - gioVao[0] * 60 - gioVao[1]

    def output(self) :
        print(self.ma, self.ten, int(self.thoiGian / 60), 'gio', self.thoiGian % 60, 'phut')

n = int(input())
a = []
for i in range(n) :
    ma = input()
    ten = input()
    gioVao = [int(x) for x in input().split(':')]
    gioRa = [int(x) for x in input().split(':')]
    a.append(Gamer(ma, ten, gioVao, gioRa))

a = sorted(a, key= lambda x : (- x.thoiGian))
for i in a :
    i.output()

''' Do Xuan Huong
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@##################@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@#############################@@@@@@@@@@@@@@@@
@@@@@@@@@@@@&####################################@@@@@@@@@@@@
@@@@@@@@@@##########################################@@@@@@@@@
@@@@@@@@##############################################@@@@@@@
@@@@@@#################################################@@@@@@
@@@@@####################################################@@@@
@@@%#####################@@@@@@@@@@@######################@@@
@@@###################@@@@@@@@@@@@@@@@@####################@@
@@##################@@@@@@         @@@@@@##################@@
@@#################@@@@@             @@@@###################@
@@@@@@@@@@@@@@@@@@@@@@@@             @@@@@@@@@@@@@@@@@@@@@@@@
@                  &@@@@             @@@@           .......@@
@@                  @@@@@@         @@@@@@           .......@@
@@                    @@@@@@@@@@@@@@@@@            .......@@@
@@@                      @@@@@@@@@@@               ......@@@@
@@@@                                              ......@@@@@
@@@@@@                                           ......@@@@@@
@@@@@@@                                         .....@@@@@@@@
@@@@@@@@@                                     .....@@@@@@@@@@
@@@@@@@@@@@@                                ....@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@                         ....@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@%                .@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''
