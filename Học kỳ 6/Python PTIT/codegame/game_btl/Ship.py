import pygame
import os
import time
import random
from pygame import mixer
from laser import Laser
WIDTH, HEIGHT = 750,750
class Ship:
    COOLDOWN = 30 # bang 1/2 FPS
    def __init__(self,x,y,health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0 #bộ đếm thời gian hồi chiêu
    
    def draw(self,window):
        window.blit(self.ship_img, (self.x,self.y))
        for laser in self.lasers:
            laser.draw(window)
    

    #laser di chuyen , muoons kiem tra xem co va cham voi cac vat the obj
    def move_lasers(self,vel,obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT): # kiểm tra tia laser có đi hết màn hình chưa, nếu rồi thì xóa đi
                self.lasers.remove(laser)
            elif laser.collision(obj): # nếu tia laser va chạm đối tượng thì sẽ làm giảm sức mạnh đi
                obj.health -= 10
                self.lasers.remove(laser) # và ta sẽ xóa laser này đi sau khi va chạm
        
    

    #phương thức đêwsm thời gian hồi chiêu
    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    
    def shoot(self):
        if self.cool_down_counter == 0: # bộ đếm thời gian hồi chiêu
            laser = Laser(self.x+23, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def get_width(self): # Lấy ra chiều rộng ảnh đối tượng
        return self.ship_img.get_width()

    def get_height(self): # Lấy ra chiều cao ảnh của đối tượng
        return self.ship_img.get_height()
