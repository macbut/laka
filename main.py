import time
import random
import pygame
import math
import os

class Organizm:
    def __init__(japko, strenght, initiative, location):
        japko.ST=strenght
        japko.IE=initiative
        japko.LN=location

pygame.mixer.init()
pygame.mixer.music.load(os.path.join("Main them.mp3"))
pygame.mixer.music.set_volume(0.17)
pygame.mixer.music.play(-1)
height=1000
width=1000
gracza_x=0
gracza_y=0
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((height,width))
Delay=0
balls=pygame.image.load('New_Piskel.png')

running=True
while running:
    Delay+=1
    screen.fill((65, 229, 76))
    clock.tick(60)
    screen.blit(balls, (gracza_x, gracza_y))
    for event in pygame.event.get():
        # zdarzenie zamknięcia programu
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    # warunki do zmiany pozycji obiektu
    if keys[pygame.K_LEFT]:
        if gracza_x > 0:
            gracza_x -= 20
    if keys[pygame.K_RIGHT]:
        if gracza_x < 940:
            gracza_x += 20
    if keys[pygame.K_UP]:
        if gracza_y > 0:
            gracza_y -= 20
    if keys[pygame.K_DOWN]:
        if gracza_y < 940:
            gracza_y += 20
    pygame.display.flip()
    time.sleep(0.05)

pygame.quit()
