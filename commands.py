import pygame
import random

pygame.font.init()
font = pygame.font.SysFont(None, 36)
# Funkcja do rysowania tekstu
def draw_text(surface, text, position, color=(255, 255, 255)):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, position)

def loc_gen(organisms):
    position = (random.randrange(0,1000,50),random.randrange(0,1000,50))
    if organisms[position[0]/50][position[1]/50] == '':
        return position
    else:
        loc_gen(organisms)