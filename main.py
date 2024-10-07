import time
import random
import pygame
import math
import os
from classes import Organism,World
from fauna import Animal,Wolf,Sheep,Viper,Mouse,Hare
from flora import Plant,Grass,Guarana,Berries
from commands import draw_text

sub1 = World.sub1
sub2 = World.sub2
sub3 = World.sub3

pygame.font.init()
font = pygame.font.SysFont(None, 36)

#muzyka
pygame.mixer.init()
pygame.mixer.music.load(os.path.join("resources/Main them.mp3"))
pygame.mixer.music.set_volume(0.17)
pygame.mixer.music.play(-1)

Delay=0
balls=pygame.image.load('resources/New_Piskel.png')

pygame.init()
clock = pygame.time.Clock()

running=True
while running:
    world = World()
    world.drawWorld()
    Delay+=1
    clock.tick(60)
    sub1.blit(balls, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_text(sub2,"Wilk zjadł owce",(10,10),(255,255,255))

    trawa = Grass(0, 0, (0, 0), sub1)
    gurana = Guarana(0,0,(50,50),sub1)
    berries = Berries(0, 0, (100, 100), sub1)
    trawa.drawing(Grass.image)
    gurana.drawing(Guarana.image)
    berries.drawing(Berries.image)
    pygame.display.flip()
    time.sleep(0.05)

pygame.quit()