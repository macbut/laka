import random
import pygame

from classes import Organism,World

class Plant(Organism):
    def action(self):
        if random.randint(1,6)==2:
            return type(self)(0,0,(550,50),World.sub1)
        else:
            return 0
class Grass(Plant):
    image=pygame.image.load('resources/tallgrass.png')
class Guarana(Plant):
    # image = pygame.image.load('')
    pass
class Berries(Plant):
    # image = pygame.image.load('')
    pass
