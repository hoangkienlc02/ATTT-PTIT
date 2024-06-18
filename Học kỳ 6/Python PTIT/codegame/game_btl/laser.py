import pygame
import os
import time
import random
from pygame import mixer
class Laser:
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
        #
        self.ok = '000'
        #
    def draw(self,window):
        window.blit(self.img,(self.x, self.y))

    def move(self,vel):
        self.y += vel
    def move1(self,vel):
        self.y+= vel
        self.x+=vel
    def move1a(self,vel):
        self.y+=vel
        self.x+=vel+3
    def move2(self,vel):
        self.y+=vel
        self.x-=vel
    def move2a(self,vel):
        self.y += vel
        self.x -= (vel+3)
    def off_screen(self,height):
        return not (self.y <= height and self.y >= 0) #kiem tra tia laser có còn nằm trong màn hình ko
    
    #phuong thuc va chạm
    def collision(self, obj):
        return collide(self, obj)
    
#cham nhau ?
def collide(obj1, obj2):
    #coi nhu vecto 2 thanh phan offerX offerY
    offset_x = obj2.x - obj1.x # phần bù X
    offset_y = obj2.y - obj1.y # phần bù Y
    return obj1.mask.overlap(obj2.mask,(offset_x,offset_y)) != None