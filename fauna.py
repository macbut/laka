from classes import Organism
import pygame

class Animal(Organism):
    pass

class Wolf(Animal):
    image = pygame.image.load('resources/wolf.png')

class Sheep(Animal):
    image=pygame.image.load('resources/owcag.png')

class Viper(Animal):
    image=pygame.image.load('resources/viper.png')

class Mouse(Animal):
    pass

class Boar(Animal):
    image=pygame.image.load('resources/boar.png')

