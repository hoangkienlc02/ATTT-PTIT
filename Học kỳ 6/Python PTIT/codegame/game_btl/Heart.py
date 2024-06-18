import pygame
import os
import time
import random
from pygame import mixer
Trai_tim = pygame.image.load(os.path.join("Icon","trai tim.png"))
class Heart():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ship_img = Trai_tim
        self.mask = pygame.mask.from_surface(Trai_tim)
    def draw(self,window):
        window.blit(Trai_tim, (self.x,self.y))
    

    #Heart dich chuyen
    def move(self,vel):
        self.y += vel
    
    def get_width(self): # Lấy ra chiều rộng ảnh đối tượng
        return self.ship_img.get_width()

    def get_height(self): # Lấy ra chiều cao ảnh của đối tượng
        return self.ship_img.get_height()
    #phuong thuc va chạm
    def collision(self, obj):
        return collide(self, obj)

#cham nhau ?
def collide(obj1, obj2):
    #coi nhu vecto 2 thanh phan offerX offerY
    offset_x = obj2.x - obj1.x # phần bù X
    offset_y = obj2.y - obj1.y # phần bù Y
    return obj1.mask.overlap(obj2.mask,(offset_x,offset_y)) != None