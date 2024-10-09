import time
import random
import pygame
import math
import os
from classes import Organism,World
from fauna import Animal,Wolf,Sheep,Viper,Mouse,Boar
from flora import Plant,Grass,Guarana,Berries
from commands import draw_text,loc_gen

sub1 = World.sub1
sub2 = World.sub2
sub3 = World.sub3

pygame.font.init()
font = pygame.font.SysFont(None, 36)

# muzyka
pygame.mixer.init()
pygame.mixer.music.load(os.path.join("resources/Main them.mp3"))
pygame.mixer.music.set_volume(0.17)
pygame.mixer.music.play(-1)

delay=0

pygame.init()
clock = pygame.time.Clock()

running=True
while running:
    world = World()
    world.drawWorld()
    delay += 1
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_text(sub2,"Wilk zjadł owce",(10,10),(255,255,255))

    if delay == 1:
        position = (random.randrange(0, 1000, 50), random.randrange(0, 1000, 50))
        organism = Grass(position, sub1)
        World.organisms[position[0]/50][position[1]/50] = organism

        dzik = Boar(loc_gen(World.organisms), sub1)
        owca = Sheep(loc_gen(World.organisms), sub1)
        zmija = Viper(loc_gen(World.organisms), sub1)
        wilk = Wolf(loc_gen(World.organisms), sub1)
        guarana = Guarana(loc_gen(World.organisms), sub1)
        jagody = Berries(loc_gen(World.organisms), sub1)
        mysz = Mouse(loc_gen(World.organisms), sub1)



    # World.organisms[5][5] = trawa.action()
    # if World.organisms[5][5] == 0:
    #     print(3)
    # else:
    #     print("udałos się")
    #     (World.organisms[5][5]).drawing()

    pygame.display.flip()
    time.sleep(0.05)

pygame.quit()
