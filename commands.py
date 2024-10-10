import pygame
import random

from classes import World

pygame.font.init()
font = pygame.font.SysFont(None, 36)
# Funkcja do rysowania tekstu
def draw_text(surface, text, position, color=(255, 255, 255)):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, position)

def loc_gen(organisms):
    position = (random.randrange(0,1000,50),random.randrange(0,1000,50))
    if organisms[int(position[0]/50)][int(position[1]/50)] == '':
        return position
    else:
        return loc_gen(organisms)