import random

from classes import Organism, World
import pygame

napis = World._napis

class Animal(Organism):
    def action(self):
        if self.ate_gua == 0:
            self.strength -= 3
        self.ate_gua -= 1
        tomove = self.gamble()
        col_org = World._organisms[tomove[0]][tomove[1]]
        #ruch
        def move():
            World._organisms[tomove[0]][tomove[1]] = self
            World._organisms[self.position[0]][self.position[1]] = ''
            self.position = tomove
        #rozmnazanie
        def breeding():
            empty = self.loc_check()
            if len(empty) == 0:
                return 0
            else:
                napis.append(f"{type(self).__name__} has breeded on {self.position[0]},{self.position[1]}")
                if len(empty) >= 2 and type(self).__name__ == 'Boar': #specjalna umiejetnosc dzika
                    for j in range(2):
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
                        World._organisms[position[0]][position[1]] = type(self)(position, World._sub1)
                        empty.remove(loc)
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
                    World._organisms[position[0]][position[1]] = type(self)(position, World._sub1)
        def collision():
            if type(col_org) == type(self):
                breeding()
            elif type(col_org).__name__ == 'Guarana':
                self.strength += 3
                self.ate_gua = 1
                move()
            elif type(col_org).__name__ == 'Berries': #dzialanie wilczych jagod
                World._organisms[self.position[0]][self.position[1]] = ''
                World._organisms[tomove[0]][tomove[1]] = ''
            else:
                if self.strength >= col_org.strength:
                    if type(col_org).__name__ == 'Viper': #specjalna umiejetnosc zmiji
                        World._organisms[self.position[0]][self.position[1]] = ''
                        World._organisms[tomove[0]][tomove[1]] = ''
                    elif type(col_org).__name__ == 'Mouse': #specjalna umiejetnosc myszy
                        if type(self).__name__ == 'Viper':
                            move()
                        else:
                            empty = col_org.loc_check()
                            if len(empty) == 0:
                                move()
                            else:
                                i = random.randint(0, len(empty) - 1)
                                loc = empty[i]
                                if loc == 'r':
                                    position = (col_org.position[0] + 1, col_org.position[1])
                                elif loc == 'l':
                                    position = (col_org.position[0] - 1, col_org.position[1])
                                elif loc == 'u':
                                    position = (col_org.position[0], col_org.position[1] - 1)
                                elif loc == 'd':
                                    position = (col_org.position[0], col_org.position[1] + 1)
                                World._organisms[position[0]][position[1]] = col_org
                                World._organisms[tomove[0]][tomove[1]] = self
                                World._organisms[self.position[0]][self.position[1]] = ''
                                self.position = tomove
                                col_org.position = position
                    else:
                        move()
                    if type(col_org).__name__ != 'Grass':
                        napis.append(f"{type(self).__name__} on {self.position[0]},{self.position[1]} ate {type(col_org).__name__}")
                else:
                    if type(self).__name__ == 'Viper': #specjalna umiejetnosc zmiji
                        World._organisms[self.position[0]][self.position[1]] = ''
                        World._organisms[tomove[0]][tomove[1]] = ''
                    else:
                        World._organisms[self.position[0]][self.position[1]] = ''
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

