import pygame
import os
import time
import random
from pygame import mixer
WIDTH, HEIGHT = 750,750
start_img1 = pygame.image.load(os.path.join("Icon","start_btn1.png"))
start_img2 = pygame.image.load(os.path.join("Icon","start_btn2.png"))
exit_img = pygame.image.load(os.path.join("Icon","exit_btn.png"))
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self):
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button
		WIN.blit(self.image, (self.rect.x, self.rect.y))

		return action
