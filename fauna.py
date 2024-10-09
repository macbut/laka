from classes import Organism
import pygame


class Animal(Organism):
    pass


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

