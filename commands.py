import pygame
import random

from classes import World

pygame.font.init()
font = pygame.font.SysFont(None, 36)
# Funkcja do rysowania tekstu
def draw_text(surface, text, position, color=(255, 255, 255)):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, position)

#ŻYDZI DO GAZU

#generowanie pozycji pierwszych organizmów na planszy
def loc_gen(organisms):
    position = (random.randrange(20),random.randrange(20))
    if organisms[position[0]][position[1]] == '':
        return position
    else:
        return loc_gen(organisms)
