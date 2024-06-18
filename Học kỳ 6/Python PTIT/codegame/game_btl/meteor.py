import pygame
import os
import time
import random
from pygame import mixer
Thien_Thach1 = pygame.image.load(os.path.join("Icon","grey_big_1.png"))
Thien_Thach2 = pygame.image.load(os.path.join("Icon","grey_big_2.png"))
Thien_Thach3 = pygame.image.load(os.path.join("Icon","brown_medium_2.png"))
class Meteor():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        x = random.randrange(1,3)
        self.img = Thien_Thach1
        self.mask = pygame.mask.from_surface(self.img)
        

    def draw(self,window):
        window.blit(self.img, (self.x,self.y))
    
   
    #laser di chuyen , muoons kiem tra xem co va cham voi cac vat the obj
    def move(self):
        self.y += random.randrange(4,5)
        self.x += random.randrange(-4,6)
        
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