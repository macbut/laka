import time
import random
import pygame
import math
import os
from classes_main import Organism,World
from fauna import Animal,Wolf,Sheep,Viper,Mouse,Hare
from flora import Plant,Grass,Guarana,Berries
from commands import draw_text


pygame.font.init()
font = pygame.font.SysFont(None, 36)

#muzyka
pygame.mixer.init()
pygame.mixer.music.load(os.path.join("resources/Main them.mp3"))
pygame.mixer.music.set_volume(0.17)
pygame.mixer.music.play(-1)

height=1000
width=1500
gracza_x=0
gracza_y=0
grass = pygame.image.load('resources/grassv2.jpg')

#podział ekranu
screen = pygame.display.set_mode((width,height))
canvas = pygame.Surface((width, height))

laka = pygame.Rect(0, 0, 1000, height)
console = pygame.Rect(1000, 0, 500, 0.9*height)
buttons = pygame.Rect(1000,0.9*height,500,0.1*height)

background = pygame.Surface((1000, height))
for i in range(0,1000,50):
    for j in range(0, 1000, 50):
        background.blit(grass,(i,j))

background2 = pygame.Surface((500, 0.9*height))
background2.fill((0,0,0))
background3 = pygame.Surface((500,0.1*height))
background3.fill((255,255,255))

sub1 = canvas.subsurface(laka)
sub2 = canvas.subsurface(console)
sub3 = canvas.subsurface(buttons)

Delay=0
balls=pygame.image.load('resources/New_Piskel.png')

pygame.init()
clock = pygame.time.Clock()

running=True
while running:
    Delay+=1
    clock.tick(60)
    sub1.blit(balls, (gracza_x, gracza_y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_text(sub2,"Wilk zjadł owce",(10,10),(255,255,255))

    #podział ekranu cd.
    screen.blit(sub1, (0, 0))
    screen.blit(sub2, (1000, 0))
    screen.blit(sub3, (1000,0.9*height))
    sub1.blit(background, (0, 0))
    sub2.blit(background2, (0, 0))
    sub3.blit(background3, (0, 0))
    pygame.draw.line(sub1, (255,255,255), (1000, 0), (1000, height), 1)
    pygame.draw.line(sub2, (255,255,255), (0, 0), (0, height), 1)

    trawa = Grass(0, 0, (0, 0), sub1)
    gurana = Guarana(0,0,(50,50),sub1)
    berries = Berries(0, 0, (100, 100), sub1)
    trawa.drawing(Grass.image)
    gurana.drawing(Guarana.image)
    berries.drawing(Berries.image)
    pygame.display.flip()
    time.sleep(0.05)

pygame.quit()


