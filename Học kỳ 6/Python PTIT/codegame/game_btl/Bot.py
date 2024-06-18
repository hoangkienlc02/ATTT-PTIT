import pygame
import os
import time
import random
from pygame import mixer
from Ship import Ship
from laser import Laser
WIDTH, HEIGHT = 750,750
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("Icon","ship boss.png"))
YELLOW_LASER = pygame.image.load(os.path.join("Icon","tenlua.png"))
explosions = [pygame.image.load(os.path.join("Icon","explosion1.png")), pygame.image.load(os.path.join("Icon","explosion2.png")), pygame.image.load(os.path.join("Icon","explosion3.png")),
              pygame.image.load(os.path.join("Icon","explosion4.png")), pygame.image.load(os.path.join("Icon","explosion5.png")),pygame.image.load(os.path.join("Icon","explosion6.png")),pygame.image.load(os.path.join("Icon","explosion7.png")),
              pygame.image.load(os.path.join("Icon","explosion8.png")),pygame.image.load(os.path.join("Icon","explosion9.png")),pygame.image.load(os.path.join("Icon","explosion10.png")),pygame.image.load(os.path.join("Icon","explosion11.png")),pygame.image.load(os.path.join("Icon","explosion12.png"))]

class Bot(Ship):        
    def __init__(self, x, y,health):
        super().__init__(x, y,health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img) # tao mat na cho be mat da cho
        self.max_health = health
        self.health = health
        self.vel = 5
    # di chuyển laser
    
    def move(self):
        if self.y -40 <  0:
            self.y += self.vel
        else:
                self.x += self.vel
                if self.x >=  WIDTH - self.get_width() or self.x <=  0:
                    self.vel*=-1
    def draw(self, window): # ghi dde phuong thuc draw o tren
        super().draw(window)
        self.healthbar(window) #cap nhap trang thai thanh suc khoe để ghi lần sau

    
    def healthbar(self,window):
        #vẽ hcn
        pygame.draw.rect(window, (255,0,0), (self.x, self.y - 10, self.ship_img.get_width(), 10)) #thanh khung cua suc manh
        pygame.draw.rect(window, (0,255,0), (self.x, self.y - 10, self.ship_img.get_width() * (1 - ((self.max_health - self.health)/self.max_health)), 10)) #thanh mau con lai
    def shoot1(self):
        if self.cool_down_counter == 0: # bộ đếm thời gian hồi chiêu
            laser1 = Laser(self.x+32, self.y+30, self.laser_img)
            laser2 = Laser(self.x+10, self.y+20, self.laser_img) 
            laser3 = Laser(self.x+54, self.y+20, self.laser_img)    
            self.lasers.append(laser1)
            self.lasers.append(laser2)
            self.lasers.append(laser3)
            self.cool_down_counter = 1

#exploition
def explosion_animation(x, y):
    for explosion in explosions:
        
        WIN.blit(explosion, (x, y))
        pygame.display.update()
        if explosion == explosions[11]:
            break
    