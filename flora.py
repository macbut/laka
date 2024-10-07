import random
import pygame

from classes_main import Organism

class Plant(Organism):
    # def action(self,id):
    #     if random.randint(1,6)==2:
    #         pass
    pass
class Grass(Plant):
    image=pygame.image.load('resources/grass - próbne.png')
class Guarana(Plant):
    image = pygame.image.load('resources/guarana - próbne.png')
class Berries(Plant):
    image = pygame.image.load('resources/Berries - próbne.png')