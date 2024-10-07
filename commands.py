import pygame

pygame.font.init()
font = pygame.font.SysFont(None, 36)
# Funkcja do rysowania tekstu
def draw_text(surface, text, position, color=(255, 255, 255)):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, position)