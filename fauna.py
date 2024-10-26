import random

from classes import Organism, World
import pygame


class Animal(Organism):
    def action(self):
        tomove = self.gamble()
        col_org = World.organisms[tomove[0]][tomove[1]]
        def move():
            World.organisms[tomove[0]][tomove[1]] = self
            World.organisms[self.position[0]][self.position[1]] = ''
            self.position = tomove
        def breeding():
            empty = self.loc_check()
            if len(empty) == 0:
                return 0
            else:
                i = random.randint(0, len(empty) - 1)
                loc = empty[i]
                if loc == 'r':
                    position = (self.position[0] + 1, self.position[1])
                elif loc == 'l':
                    position = (self.position[0] - 1, self.position[1])
                elif loc == 'u':
                    position = (self.position[0], self.position[1] - 1)
                elif loc == 'd':
                    position = (self.position[0], self.position[1] + 1)
                World.organisms[position[0]][position[1]] = type(self)(position, World.sub1)
        def collision():
            if type(col_org) == type(self):
                breeding()
            else:
                if self.strength > col_org.strength:
                    print(self.strength,'  ',col_org.strength)
                    move()
                elif self.strength == col_org.strength:
                    pass
                else:
                    World.organisms[self.position[0]][self.position[1]] = ''
        if col_org == '':
            move()
        else:
            collision()
        self.age+=1


class Wolf(Animal):
    image = pygame.image.load('resources/wolf.png')
    strength = 9
    ini = 5


class Sheep(Animal):
    image = pygame.image.load('resources/owcag.png')
    strength = 4
    ini = 4

class Viper(Animal):
    image = pygame.image.load('resources/viper.png')
    strength = 2
    ini = 3

class Mouse(Animal):
    image = pygame.image.load('resources/mouse.png')
    strength = 1
    ini = 6

class Boar(Animal):
    image = pygame.image.load('resources/boar.png')
    strength = 5
    ini = 2

