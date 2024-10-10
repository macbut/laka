import pygame


class World:
    height = 1000
    width = 1500
    grass = pygame.image.load('resources/grassv2.jpg')

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
        full = []
        if x - 1 < 0:
            full.append('l')
        elif organisms[x - 1][y] != '':
            full.append('l')
        else:
            empty.append('l')
        if x + 1 > 19:
            full.append('r')
        elif organisms[x + 1][y] != '':
            full.append('r')
        else:
            empty.append('r')
        if y - 1 < 0:
            full.append('u')
        elif organisms[x][y - 1] != '':
            full.append('u')
        else:
            empty.append('u')
        if y + 1 > 19:
            full.append('d')
        elif organisms[x][y + 1] != '':
            full.append('d')
        else:
            empty.append('d')

        print(empty)
        print(full)
