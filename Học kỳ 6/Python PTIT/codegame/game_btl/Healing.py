import pygame
import os
import time
import random
from pygame import mixer
Hoi_mau = pygame.image.load(os.path.join("Icon","hoi_mau.png"))
class Healing():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.ship_img = Hoi_mau
        self.mask = pygame.mask.from_surface(Hoi_mau)
        

    def draw(self,window):
        window.blit(Hoi_mau, (self.x,self.y))
    
   
    #laser di chuyen , muoons kiem tra xem co va cham voi cac vat the obj
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