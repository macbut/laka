import random
import pygame

from classes import Organism,World


class Plant(Organism):
    strength = 0
    initiative = 0
    def action(self):
        if random.randint(1,6)==2:
            return type(self)((550,50),World.sub1)
        else:
            return 0


class Grass(Plant):
    image = pygame.image.load('resources/tallgrass.png')


class Guarana(Plant):
    image = pygame.image.load('resources/guarana.png')


class Berries(Plant):
    image = pygame.image.load('resources/wilczejagody.png')
