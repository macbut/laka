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
                    print(If_pressed_one)
                    time.sleep(0.15)
        delay += 1
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_text(sub2,"Wilk zjadł owce",(10,10),(255,255,255))
        if If_pressed_one==1:
            for i in range(20):
                for j in range(20):
                    if type(world.organisms[i][j]).__name__ == "Wolf":
                        world.organisms[i][j].action()
                    if type(world.organisms[i][j]).__name__ == "Sheep":
                        world.organisms[i][j].action()
                    if type(world.organisms[i][j]).__name__ == "Viper":
                        world.organisms[i][j].action()
                    if type(world.organisms[i][j]).__name__ == "Mouse":
                        world.organisms[i][j].action()
                    if type(world.organisms[i][j]).__name__ == "Boar":
                        world.organisms[i][j].action()

            tab=[]
            for i in range(20):
                for j in range(20):
                    if type(world.organisms[i][j]).__name__ == "Grass":
                        tab.append((i,j))
            for i in tab:
                if type(world.organisms[i[0]][i[1]]).__name__ == "Grass":
                    organism = world.organisms[i[0]][i[1]].action(6)
                    if type(organism) != int:
                        world.organisms[organism.position[0]][organism.position[1]] = organism
            for i in range(20):
                for j in range(20):
                    if type(world.organisms[i][j]).__name__ == "Guarana":
                        tab.append((i,j))
            for i in tab:
                if type(world.organisms[i[0]][i[1]]).__name__ == "Guarana":
                    organism = world.organisms[i[0]][i[1]].action(10)
                    if type(organism) != int:
                        world.organisms[organism.position[0]][organism.position[1]] = organism
            for i in range(20):
                for j in range(20):
                    if type(world.organisms[i][j]).__name__ == "Berries":
                        tab.append((i,j))
            for i in tab:
                if type(world.organisms[i[0]][i[1]]).__name__ == "Berries":
                    organism = world.organisms[i[0]][i[1]].action(10)
                    if type(organism) != int:
                        world.organisms[organism.position[0]][organism.position[1]] = organism
        print("---------------------------------",delay,"---------------------------------")
        world.drawWorld()
        pygame.display.update()
        If_pressed_one=0

pygame.quit()
