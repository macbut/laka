import time
import random
from time import sleep

import pygame
import math
import os
from classes import Organism,World
from fauna import Animal,Wolf,Sheep,Viper,Mouse,Boar
from flora import Plant,Grass,Guarana,Berries
from commands import draw_text,loc_gen

napis = World._napis

sub1 = World._sub1
sub2 = World._sub2
sub3 = World._sub3

organisms = [Grass,Guarana,Berries,Wolf,Sheep,Viper,Mouse,Boar]

pygame.font.init()
font = pygame.font.SysFont(None, 36)

# muzyka
pygame.mixer.init()
pygame.mixer.music.load(os.path.join("resources/Main them.mp3"))
pygame.mixer.music.set_volume(0.17)
pygame.mixer.music.play(-1)
vic_sound = pygame.mixer.Sound("resources/victory-royale.mp3")
vic_sound.set_volume(0.1)
vic_count = 0

delay=0
os.environ['SDL_AUDIODRIVER'] = 'dsp'
pygame.init()
clock = pygame.time.Clock()
pressed_one=False
pressed_two=False
counter = 0
# losowanie pozycji pierwszych organizmów
for i in range(3):
    for j in range(8):
        position = loc_gen(World._organisms)
        organism = organisms[j](position, sub1)
        organism.age = 2
        World._organisms[position[0]][position[1]] = organism

running=True
while running:
    world = World()

    victory = True
    for i in range(20):
        if not victory:
            break
        for j in range(19):
            if type(World._organisms[i][j]).__name__ != type(World._organisms[i][j + 1]).__name__:
                victory = False
                break

    if victory:
        World._sub1.blit(World._royale, (150, 298))
        vic_count+=1
        if vic_count == 1:
            vic_sound.play()
            pygame.mixer.music.stop()

    #sprawdzanie który przycisk został kliknięty
    if pygame.mouse.get_pos()[0]>810 and pygame.mouse.get_pos()[1]>690 and pygame.mouse.get_pos()[0]<1010 and pygame.mouse.get_pos()[1]<790:
        if (pygame.mouse.get_pressed(num_buttons=3)[0])==True:
                pressed_one=True
                time.sleep(0.15)
    if pygame.mouse.get_pos()[0]>1010 and pygame.mouse.get_pos()[1]>690 and pygame.mouse.get_pos()[0]<1210 and pygame.mouse.get_pos()[1]<790:
        if (pygame.mouse.get_pressed(num_buttons=3)[0])==True:
                pressed_two=True
                time.sleep(0.15)
    delay += 1
    clock.tick(60)
    #zamykanie programu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #generowanie napisu
    y=10
    zmiana=30
    max_y=650
    if len(napis)>0 and (y+len(napis)*zmiana)>max_y:
        del napis[0]

    for i,tekst in enumerate(napis):
        draw_text(sub2,tekst,(10,y+i*zmiana),(255,255,255))

    sort_org = world.ruch()
    #przycisk następna tura
    if pressed_one:
        napis.clear()
        for i in sort_org[:]:
            if World._organisms[i[0].position[0]][i[0].position[1]] == i[0]:
                i[0].action()
            else:
                sort_org.remove(i)
            sort_org.sort(key=lambda x: x[0].ini, reverse=True)
    #przycisk następny organizm
    if pressed_two:
        if counter > len(sort_org)-1:
            counter = 0
        else:
            if sort_org[counter][2] != 1:
                sort_org[counter][0].action()
            pressed_two = False
            counter += 1

    # print("---------------------------------",delay,"---------------------------------")
    world.drawWorld()
    pygame.display.update()
    pressed_one=0

pygame.quit()
