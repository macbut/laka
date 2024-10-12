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

pygame.init()
clock = pygame.time.Clock()

running=True
while running:
    world = World()
    delay += 1
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_text(sub2,"Wilk zjadł owce",(10,10),(255,255,255))

    # losowanie pozycji pierwszych organizmów
    if delay == 1:
        for i in range(2):
            for j in range(8):
                position = loc_gen(world.organisms)
                organism = organisms[j](position, sub1)
                world.organisms[position[0]][position[1]] = organism

    for i in range(20):
        for j in range(20):
            if type(world.organisms[i][j]).__name__ == "Grass":
                organism = world.organisms[i][j].action()
                if type(organism) != int:
                    world.organisms[organism.position[0]][organism.position[1]] = organism

    world.drawWorld()

    pygame.display.flip()
    time.sleep(2)

pygame.quit()
