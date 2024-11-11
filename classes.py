import random
import pygame

class World:
    napis = []
    height = 800
    width = 1300
    #pobieranie obrazów
    grass = pygame.image.load('resources/grassv2-inna-ramka.jpg')
    Button_next = pygame.image.load("resources/guzik_następny_na_szybko.png")
    Button_next_orgazm = pygame.image.load("resources/guzik_następny_na_szybko_ale_dwa.png")

    #ustawianie wielkości ekranu
    screen = pygame.display.set_mode((width, height))
    canvas = pygame.Surface((width, height))

    #tworzenie podziału ekranu
    laka = pygame.Rect(0, 0, 800, height)
    console = pygame.Rect(800, 0, 500, 0.85 * height)
    buttons = pygame.Rect(800, 0.85 * height, 500, 0.15 * height)

    background = pygame.Surface((800, height))
    for i in range(0, 800, 40):
        for j in range(0, 800, 40):
            background.blit(grass, (i, j))

    background2 = pygame.Surface((500, 0.85 * height))
    background2.fill((0, 0, 0))
    background3 = pygame.Surface((500, 0.15 * height))
    background3.fill((255, 255, 255))

    sub1 = canvas.subsurface(laka)
    sub2 = canvas.subsurface(console)
    sub3 = canvas.subsurface(buttons)

    #tworzenie tablicy przechowującej organizmy
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
    #rysowanie swiata
    def drawWorld(self):
        World.screen.blit(World.sub1, (0, 0))
        World.screen.blit(World.sub2, (800, 0))
        World.screen.blit(World.sub3, (800, 0.85 * World.height))
        World.sub1.blit(World.background, (0, 0))
        World.sub2.blit(World.background2, (0, 0))
        World.sub3.blit(World.background3, (0, 0))
        World.sub3.blit(World.background3, (0, 0))
        World.canvas.blit(World.Button_next,(810,0.85 * World.height + 10))
        World.canvas.blit(World.Button_next_orgazm, (910, 0.85 * World.height + 10))
        pygame.draw.line(World.sub1, (255, 255, 255), (800, 0), (800, World.height), 1)
        pygame.draw.line(World.sub2, (255, 255, 255), (0, 0), (0, World.height), 1)
        for i in range(20):
            for j in range(20):
                if World.organisms[i][j] == '':
                    pass
                else:
                    World.organisms[i][j].drawing()

    #sortowanie tablicy
    def ruch(self):
        org = []
        sort_org = []
        for i in range(20):
            for j in range(20):
                if World.organisms[i][j] != '':
                    org.append(World.organisms[i][j])
        for i in org:
            sort_org.append((i, i.ini, i.age))
        size = len(sort_org)
        for i in range(size):
            for j in range(0, size - i - 1):
                if sort_org[j][1] > sort_org[j + 1][1]:
                    sort_org[j], sort_org[j + 1] = sort_org[j + 1], sort_org[j]
                if sort_org[j][1] == sort_org[j + 1][1]:
                    if sort_org[j][2] > sort_org[j + 1][2]:
                        sort_org[j], sort_org[j + 1] = sort_org[j + 1], sort_org[j]
        return sort_org[::-1]

class Organism:
    current_id = 1
    def __init__(self, position, world):
        self.id=Organism.current_id
        Organism.current_id += 1
        self.position=position
        self.world=world
        self.age=1
        self.ate_gua = -1
    def drawing(self):
        self.world.blit(self.image,(self.position[0]*40,self.position[1]*40))

    #sprawdzenie wolenych pól
    def loc_check(self):
        organisms = World.organisms
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

    #wybieranie miejsca do ruchu organizmu
    def gamble(self):
        i = random.randint(1,4)
        if i == 1:
            if self.position[0]+1 <= 19:
                return self.position[0]+1,self.position[1]
            else:
                return self.gamble()
        elif i == 2:
            if self.position[0]-1 >= 0:
                return self.position[0]-1,self.position[1]
            else:
                return self.gamble()
        elif i == 3:
            if self.position[1]+1 <= 19:
                return self.position[0],self.position[1]+1
            else:
                return self.gamble()
        elif i == 4:
            if self.position[1]-1 >= 0:
                return self.position[0],self.position[1]-1
            else:
                return self.gamble()
