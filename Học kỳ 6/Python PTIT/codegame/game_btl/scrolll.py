import pygame
import os
import time
import random
from pygame import mixer
width = 200
height = 300

screen = pygame.display.set_mode([width,height])
pygame.display.set_caption("scrolling background")
background = pygame.transform.scale(pygame.image.load(os.path.join("assets","background-black.png")), (width,height))
overlap = pygame.transform.scale(pygame.image.load(os.path.join("assets","background-black.png")), (width,height))
b_pos = 0
o_pos = 300
speed = 0.1
running = True

while running:
    if b_pos <= -height:
        b_pos = height
    if o_pos <= -height:
        o_pos = height

    b_pos -= speed
    o_pos -= speed
    screen.blit(background, (0,b_pos))
    screen.blit(overlap, (0,o_pos))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()

