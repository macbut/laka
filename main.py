import time
import random
import pygame
import os
import math

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1000,1000))
i=0
running=True
while running:
    i+=1
    screen.fill((65, 229, 76))
    clock.tick(60)
    for event in pygame.event.get():
        # zdarzenie zamknięcia programu
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
