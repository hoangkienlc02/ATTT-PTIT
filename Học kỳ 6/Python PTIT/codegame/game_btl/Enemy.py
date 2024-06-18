import pygame
import os
import time
import random
from pygame import mixer
from laser import Laser
from Ship import Ship
RED_SPACE_SHIP = pygame.image.load(os.path.join("Icon","tau den.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("Icon","tau tim.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("Icon","tau xanh.png"))
RED_LASER = pygame.image.load(os.path.join("Icon","laser_enemy.png"))
GREEN_LASER = pygame.image.load(os.path.join("Icon","laser_enemy.png"))
BLUE_LASER = pygame.image.load(os.path.join("Icon","laser_enemy.png"))  
class Enemy(Ship):
    COLOR_MAP = {
                 "red": (RED_SPACE_SHIP,RED_LASER),
                 "green": (GREEN_SPACE_SHIP,GREEN_LASER),
                 "blue": (BLUE_SPACE_SHIP,BLUE_LASER)
                }

    def __init__(self, x, y,color,health=100):
        super().__init__(x,y,health) # đoạn lệnh này thay cho self.x= x,  self.y = y health = 100
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
    def move(self,vel):
        self.y += vel
    def shoot(self):
        if self.cool_down_counter == 0: # bộ đếm thời gian hồi chiêu
            laser = Laser(self.x+32, self.y+30, self.laser_img)     
            self.lasers.append(laser)
            self.cool_down_counter = 1
