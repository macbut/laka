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

organisms = [Grass,Guarana,Berries,Wolf,Sheep,Viper,Mouse,Boar]

pygame.font.init()
font = pygame.font.SysFont(None, 36)

# muzyka
pygame.mixer.init()
pygame.mixer.music.load(os.path.join("resources/Main them.mp3"))
pygame.mixer.music.set_volume(0.17)
pygame.mixer.music.play(-1)

delay=0
os.environ['SDL_AUDIODRIVER'] = 'dsp'
pygame.init()
clock = pygame.time.Clock()
If_pressed_one=0
# losowanie pozycji pierwszych organizmów
for i in range(2):
    for j in range(8):
        position = loc_gen(World.organisms)
        organism = organisms[j](position, sub1)
        World.organisms[position[0]][position[1]] = organism

running=True
while running:
        world = World()
        if pygame.mouse.get_pos()[0]>810 and pygame.mouse.get_pos()[1]>690 and pygame.mouse.get_pos()[0]<910 and pygame.mouse.get_pos()[1]<740:
            if (pygame.mouse.get_pressed(num_buttons=3)[0])==True:
                    If_pressed_one=1
                    time.sleep(0.15)
        delay += 1
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_text(sub2,"Wilk zjadł owce",(10,10),(255,255,255))
        if If_pressed_one==1:
            org=[]
            sort_org=[]
            for i in range(20):
                for j in range(20):
                    if world.organisms[i][j] != '':
                        org.append(world.organisms[i][j])
            for i in org:
                sort_org.append((i,i.ini,i.age))
            size=len(sort_org)
            for i in range(size):
                for j in range(0, size - i - 1):
                    if sort_org[j][1] > sort_org[j + 1][1]:
                        sort_org[j], sort_org[j + 1] = sort_org[j + 1], sort_org[j]
            sort_org=sort_org[::-1]
            for i in sort_org:
                i[0].action()
        # print("---------------------------------",delay,"---------------------------------")
        world.drawWorld()
        pygame.display.update()
        If_pressed_one=0

pygame.quit()
