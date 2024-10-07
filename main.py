import time
import random
import pygame
import math
import os

class World:
    def __init__(self,organisms):
        self.OR=organisms
    def nextTurn(self):
        pass
    def drawWorld(self):
        self.Table_of_world=[]
        for i in range(1,21):
            Helping_table=[]
            for j in range(1,21):
                Helping_table.append(0)
            self.Table_of_world.append(Helping_table)

class Organism:
    current_id = 1
    def __init__(self, strenght, initiative, location, world):
        self.id=Organism.current_id
        Organism.current_id += 1
        #self.type=type
        self.ST=strenght
        self.IN=initiative
        self.LN=location
        self.WD=world
    def action(self):
        pass
    def colision(self):
        pass
    def drawing(self):
        pass

pygame.font.init()
font = pygame.font.SysFont(None, 36)

# Funkcja do rysowania tekstu
def draw_text(surface, text, position, color=(255, 255, 255)):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, position)

#muzyka
pygame.mixer.init()
pygame.mixer.music.load(os.path.join("resources/Main them.mp3"))
pygame.mixer.music.set_volume(0.17)
pygame.mixer.music.play(-1)

height=1000
width=1500
gracza_x=0
gracza_y=0
grass = pygame.image.load('resources/grass.jpg')

#podział ekranu
screen = pygame.display.set_mode((width,height))
canvas = pygame.Surface((width, height))

laka = pygame.Rect(0, 0, 1000, height)
console = pygame.Rect(1000, 0, 500, 900)
buttons = pygame.Rect(1000,900,500,100)

background = pygame.Surface((1000, height))
for i in range(0,1000,50):
    for j in range(0, 1000, 50):
        background.blit(grass,(i,j))

background2 = pygame.Surface((500, 900))
background2.fill((0,0,0))
background3 = pygame.Surface((500,100))
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

    draw_text(sub2,"Wilk zjadł owce",(10,10),(255,255,255))

    #podział ekranu cd.
    screen.blit(sub1, (0, 0))
    screen.blit(sub2, (1000, 0))
    screen.blit(sub3, (1000,900))
    sub1.blit(background, (0, 0))
    sub2.blit(background2, (0, 0))
    sub3.blit(background3, (0, 0))
    pygame.draw.line(sub1, (255,255,255), (1000, 0), (1000, height), 1)
    pygame.draw.line(sub2, (255,255,255), (0, 0), (0, height), 1)

    pygame.display.flip()
    time.sleep(0.05)

pygame.quit()
