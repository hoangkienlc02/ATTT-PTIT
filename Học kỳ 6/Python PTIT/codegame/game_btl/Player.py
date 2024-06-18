import pygame
import os
import time
import random
from pygame import mixer
from Ship import Ship
from laser import Laser
from Bot import Bot
WIDTH, HEIGHT = 750,750
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("Icon","tau_minh (1).png"))
DANTRON = pygame.image.load(os.path.join("Icon","Đạn tròn.png"))

YELLOW_LASER = pygame.image.load(os.path.join("Icon","laser1.png"))
nhan_laser =  pygame.image.load(os.path.join("Icon","pixil-frame-0 (1).png"))
explosions = [pygame.image.load(os.path.join("Icon","explosion1.png")), pygame.image.load(os.path.join("Icon","explosion2.png")), pygame.image.load(os.path.join("Icon","explosion3.png")),
              pygame.image.load(os.path.join("Icon","explosion4.png")), pygame.image.load(os.path.join("Icon","explosion5.png")),pygame.image.load(os.path.join("Icon","explosion6.png")),pygame.image.load(os.path.join("Icon","explosion7.png")),
              pygame.image.load(os.path.join("Icon","explosion8.png")),pygame.image.load(os.path.join("Icon","explosion9.png")),pygame.image.load(os.path.join("Icon","explosion10.png")),pygame.image.load(os.path.join("Icon","explosion11.png")),pygame.image.load(os.path.join("Icon","explosion12.png"))]
class Player(Ship):        
    def __init__(self, x, y,health=100):
        super().__init__(x, y,health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img) # tao mat na cho be mat da cho
        self.max_health = health
    # di chuyển laser
    def move_lasers(self,vel,objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT): # kiểm tra tia laser có đi hết màn hình chưa, nếu rồi thì xóa đi
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if  laser.collision(obj): # nếu tia laser va chạm đối tượng thì sẽ làm giảm sức mạnh đi
                        objs.remove(obj) #se xóa máy bay địch đó đi
                        explosion_Sound = mixer.Sound(os.path.join("sound","explosion.wav"))#os.path.join("Icon","explosion.wav")
                        explosion_Sound.play()
                        enemy_1x = obj.x
                        enemy_1y = obj.y
                        explosion_animation(enemy_1x, enemy_1y)
                        if laser in self.lasers:#kiểm tra phải có laser mới xóa
                            self.lasers.remove(laser) # và ta sẽ xóa laser này đi sau khi va chạm
    def move_lasers1(self,vel,objs):
        self.cooldown()
        for laser in self.lasers:
            #laser.mov
            if laser.ok == '010': laser.move(vel)
            elif laser.ok == '100': laser.move2(vel)
            elif laser.ok == '100a': laser.move2a(vel)
            elif laser.ok == '001' : laser.move1(vel)
            elif laser.ok == '001a': laser.move1a(vel)
            else: laser.move(vel)
            if laser.off_screen(HEIGHT): # kiểm tra tia laser có đi hết màn hình chưa, nếu rồi thì xóa đi
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if  laser.collision(obj): # nếu tia laser va chạm đối tượng thì sẽ làm giảm sức mạnh đi
                        objs.remove(obj) #se xóa máy bay địch đó đi
                        explosion_Sound = mixer.Sound(os.path.join("sound","explosion.wav"))#os.path.join("Icon","explosion.wav")
                        explosion_Sound.play()
                        enemy_1x = obj.x
                        enemy_1y = obj.y
                        explosion_animation(enemy_1x, enemy_1y)
                        if laser in self.lasers:#kiểm tra phải có laser mới xóa
                            self.lasers.remove(laser) # và ta sẽ xóa laser này đi sau khi va chạm
    def mvb(self,objs):
        for obj in objs:
            if collide(obj, self):
                self.health-=1
                obj.health-=1

    def draw(self, window): # ghi dde phuong thuc draw o tren
        super().draw(window)
        self.healthbar(window) #cap nhap trang thai thanh suc khoe để ghi lần sau

    
    def healthbar(self,window):
        #vẽ hcn
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10)) #thanh khung cua suc manh
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (1 - ((self.max_health - self.health)/self.max_health)), 10)) #thanh mau con lai
    def shoot1(self):
        if self.cool_down_counter == 0: # bộ đếm thời gian hồi chiêu
            laser1 = Laser(self.x+23, self.y, DANTRON)
            laser1.ok = '010'
            laser21 = Laser(self.x+12, self.y+15, DANTRON)
            laser21.ok = '100a'
            laser2 = Laser(self.x+8, self.y+15, DANTRON)
            laser2.ok = '100'
            laser3 = Laser(self.x+43, self.y+15, DANTRON)
            laser3.ok = '001'
            laser31 = Laser(self.x+29, self.y+15, DANTRON)
            laser31.ok = '001a'
            self.lasers.append(laser1)
            self.lasers.append(laser2)
            self.lasers.append(laser3)
            self.lasers.append(laser21)
            self.lasers.append(laser31)
            self.cool_down_counter = 1
#exploition
def explosion_animation(x, y):
    for explosion in explosions:
        
        WIN.blit(explosion, (x, y))
        pygame.display.update()
        if explosion == explosions[11]:
            break
def collide(obj1, obj2):
    #coi nhu vecto 2 thanh phan offerX offerY
    offset_x = obj2.x - obj1.x # phần bù X
    offset_y = obj2.y - obj1.y # phần bù Y
    return obj1.mask.overlap(obj2.mask,(offset_x,offset_y)) != None