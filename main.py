import time
import random
import pygame
import math

class Organizm:
    def __init__(self, strenght, initiative, location):
        self.ST=strenght
        self.IE=initiative
        self.LN=location


clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1000,1000))
Opuz=0
balls=pygame.image.load('Japan_small_icon.png')

running=True
while running:
    Opuz+=1
    screen.fill((65, 229, 76))
    clock.tick(60)
    screen.blit(balls, (372, 372))
    for event in pygame.event.get():
        # zdarzenie zamknięcia programu
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    time.sleep(0.1)

pygame.quit()
