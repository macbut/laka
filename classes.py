import random
import pygame

class World:
    height = 1000
    width = 1500
    grass = pygame.image.load('resources/grassv2-inna-ramka.jpg')
    Button_next = pygame.image.load("resources/guzik_następny_na_szybko.png")

    screen = pygame.display.set_mode((width, height))
    canvas = pygame.Surface((width, height))

    laka = pygame.Rect(0, 0, 1000, height)
    console = pygame.Rect(1000, 0, 500, 0.9 * height)
    buttons = pygame.Rect(1000, 0.9 * height, 500, 0.1 * height)

    background = pygame.Surface((1000, height))
    for i in range(0, 1000, 50):
        for j in range(0, 1000, 50):
            background.blit(grass, (i, j))

    background2 = pygame.Surface((500, 0.9 * height))
    background2.fill((0, 0, 0))
    background3 = pygame.Surface((500, 0.1 * height))
    background3.fill((255, 255, 255))

    sub1 = canvas.subsurface(laka)
    sub2 = canvas.subsurface(console)
    sub3 = canvas.subsurface(buttons)

    organisms = []
    for i in range(20):
        helping_table = []
        for j in range(20):
            helping_table.append('')
        organisms.append(helping_table)

    def __init__(self):
        pass
    def nextTurn(self):
        pass
    def drawWorld(self):
        World.screen.blit(World.sub1, (0, 0))
        World.screen.blit(World.sub2, (1000, 0))
        World.screen.blit(World.sub3, (1000, 0.9 * World.height))
        World.sub1.blit(World.background, (0, 0))
        World.sub2.blit(World.background2, (0, 0))
        World.sub3.blit(World.background3, (0, 0))
        World.sub3.blit(World.background3, (0, 0))
        World.canvas.blit(World.Button_next,(1010,0.9 * World.height + 10))
        pygame.draw.line(World.sub1, (255, 255, 255), (1000, 0), (1000, World.height), 1)
        pygame.draw.line(World.sub2, (255, 255, 255), (0, 0), (0, World.height), 1)
        for i in range(20):
            for j in range(20):
                if World.organisms[i][j] == '':
                    pass
                else:
                    World.organisms[i][j].drawing()

class Organism:
    current_id = 1
    def __init__(self, position, world):
        self.id=Organism.current_id
        Organism.current_id += 1
        self.position=position
        self.world=world
    def action(self):
        pass
    def colision(self):
        pass
    def drawing(self):
        self.world.blit(self.image,(self.position[0]*50,self.position[1]*50))

    def loc_check(self, organisms=World.organisms):
        position = self.position
        x = position[0]
        y = position[1]
        empty = []
        if x - 1 < 0:
            pass
        elif organisms[x - 1][y] != '':
            pass
        else:
            empty.append('l')
        if x + 1 > 19:
            pass
        elif organisms[x + 1][y] != '':
            pass
        else:
            empty.append('r')
        if y - 1 < 0:
            pass
        elif organisms[x][y - 1] != '':
            pass
        else:
            empty.append('u')
        if y + 1 > 19:
            pass
        elif organisms[x][y + 1] != '':
            pass
        else:
            empty.append('d')

        return empty

    def gamble(self):
        i = random.randint(1,4)
        if i == 1:
            if self.position[0]+1 < 19:
                return self.position[0]+1,self.position[1]
            else:
                return self.gamble()
        elif i == 2:
            if self.position[0]-1 > 0:
                return self.position[0]-1,self.position[1]
            else:
                return self.gamble()
        elif i == 3:
            if self.position[1]+1 < 19:
                return self.position[0],self.position[1]+1
            else:
                return self.gamble()
        elif i == 4:
            if self.position[1]-1 > 0:
                return self.position[0],self.position[1]-1
            else:
                return self.gamble()