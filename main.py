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
pressed_one=0
pressed_two=0
counter = 0
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
                pressed_one=1
                time.sleep(0.15)
    if pygame.mouse.get_pos()[0]>910 and pygame.mouse.get_pos()[1]>690 and pygame.mouse.get_pos()[0]<1010 and pygame.mouse.get_pos()[1]<740:
        if (pygame.mouse.get_pressed(num_buttons=3)[0])==True:
                pressed_two=1
                time.sleep(0.15)
    delay += 1
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_text(sub2,"Wilk zjadł owce",(10,10),(255,255,255))
    sort_org = world.ruch()
    if pressed_one==1:
        for i in sort_org:
            i[0].action()
            sort_org = world.ruch()
            print(i[0].__bases__)
    if pressed_two == 1:
        print(len(sort_org))
        print(counter)
        if counter > len(sort_org)-1:
            counter = 0
        else:
            sort_org[counter][0].action()
            pressed_two = 0
            counter += 1

    # print("---------------------------------",delay,"---------------------------------")
    world.drawWorld()
    pygame.display.update()
    pressed_one=0

pygame.quit()
