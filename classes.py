import random
import pygame

class World:
    _napis = []
    _height = 800
    _width = 1300
    #pobieranie obrazów
    _grass = pygame.image.load('resources/grassv2-inna-ramka.jpg')
    _Button_next = pygame.image.load("resources/nextturn.png")
    _Button_next_orgazm = pygame.image.load("resources/nextorganism.png")
    _royale = pygame.image.load("resources/VicRoy2.png")

    #ustawianie wielkości ekranu
    _screen = pygame.display.set_mode((_width, _height))
    _canvas = pygame.Surface((_width, _height))

    #tworzenie podziału ekranu
    _laka = pygame.Rect(0, 0, 800, _height)
    _console = pygame.Rect(800, 0, 500, 0.85 * _height)
    _buttons = pygame.Rect(800, 0.85 * _height, 500, 0.15 * _height)

    _background = pygame.Surface((800, _height))
    for i in range(0, 800, 40):
        for j in range(0, 800, 40):
            _background.blit(_grass, (i, j))

    _background2 = pygame.Surface((500, 0.85 * _height))
    _background2.fill((0, 0, 0))
    _background3 = pygame.Surface((500, 0.15 * _height))
    _background3.fill((255, 255, 255))

    _sub1 = _canvas.subsurface(_laka)
    _sub2 = _canvas.subsurface(_console)
    _sub3 = _canvas.subsurface(_buttons)

    #tworzenie tablicy przechowującej organizmy
    _organisms = []
    for i in range(20):
        helping_table = []
        for j in range(20):
            helping_table.append('')
        _organisms.append(helping_table)

    def __init__(self):
        pass
    def nextTurn(self):
        pass
    #rysowanie swiata
    def drawWorld(self):
        World._screen.blit(World._sub1, (0, 0))
        World._screen.blit(World._sub2, (800, 0))
        World._screen.blit(World._sub3, (800, 0.85 * World._height))
        World._sub1.blit(World._background, (0, 0))
        World._sub2.blit(World._background2, (0, 0))
        World._sub3.blit(World._background3, (0, 0))
        World._sub3.blit(World._background3, (0, 0))
        World._canvas.blit(World._Button_next, (810, 0.85 * World._height + 10))
        World._canvas.blit(World._Button_next_orgazm, (1010, 0.85 * World._height + 10))
        pygame.draw.line(World._sub1, (255, 255, 255), (800, 0), (800, World._height), 1)
        pygame.draw.line(World._sub2, (255, 255, 255), (0, 0), (0, World._height), 1)
        for i in range(20):
            for j in range(20):
                if World._organisms[i][j] == '':
                    pass
                else:
                    World._organisms[i][j].drawing()

    #sortowanie tablicy
    def ruch(self):
        org = []
        sort_org = []
        for i in range(20):
            for j in range(20):
                if World._organisms[i][j] != '':
                    org.append(World._organisms[i][j])
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

    pygame.font.init()
    _font = pygame.font.SysFont(None, 36)
    # Funkcja do rysowania tekstu
    def draw_text(self, surface, text, position, color=(255, 255, 255)):
        text_surface = World._font.render(text, True, color)
        surface.blit(text_surface, position)

    # generowanie pozycji pierwszych organizmów na planszy
    def loc_gen(self, organisms):
        position = (random.randrange(20), random.randrange(20))
        if organisms[position[0]][position[1]] == '':
            return position
        else:
            return self.loc_gen(organisms)

class Organism:
    _current_id = 1
    def __init__(self, position, world):
        self.id=Organism._current_id
        Organism._current_id += 1
        self.position=position
        self.world=world
        self.age=1
        self.ate_gua = -1
    def drawing(self):
        self.world.blit(self.image,(self.position[0]*40,self.position[1]*40))

    #sprawdzenie wolenych pól
    def loc_check(self):
        organisms = World._organisms
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
