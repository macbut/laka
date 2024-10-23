import random

from classes import Organism, World
import pygame


class Animal(Organism):
    def action(self):
        move_to = self.gamble()
        print(move_to,"gdzie ma iść")
        def move():
            World.organisms[move_to[0]][move_to[1]] = self
            World.organisms[self.position[0]][self.position[1]] = ''
            self.position = move_to
        move()


class Wolf(Animal):
    image = pygame.image.load('resources/wolf.png')
    strength = 9
    initiative = 5


class Sheep(Animal):
    image = pygame.image.load('resources/owcag.png')
    strength = 4
    initiative = 4

class Viper(Animal):
    image = pygame.image.load('resources/viper.png')
    strength = 2
    initiative = 3

class Mouse(Animal):
    image = pygame.image.load('resources/mouse.png')
    strength = 1
    initiative = 6

class Boar(Animal):
    image = pygame.image.load('resources/boar.png')
    strength = 6
    initiative = 3

