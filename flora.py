import random
import pygame

from classes import Organism,World


class Plant(Organism):
    strength = 0
    initiative = 0
    def action(self,cos):
        empty = self.loc_check()
        if len(empty) == 0:
            return 0
        elif random.randint(1,cos)==2:
            print("udało się")
            i = random.randint(0,len(empty)-1)
            loc = empty[i]
            if loc == 'r':
                position = (self.position[0]+1,self.position[1])
            elif loc == 'l':
                position = (self.position[0]-1,self.position[1])
            elif loc == 'u':
                position = (self.position[0],self.position[1]-1)
            elif loc == 'd':
                position = (self.position[0],self.position[1]+1)
            return type(self)(position,World.sub1)
        else:
            print("nie udało się")
            return 0


class Grass(Plant):
    image = pygame.image.load('resources/TallGrass_leprza.png')


class Guarana(Plant):
    image = pygame.image.load('resources/guarana.png')


class Berries(Plant):
    image = pygame.image.load('resources/wilczejagody.png')
