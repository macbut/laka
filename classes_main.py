import pygame


class World:
    def __init__(self,organisms):
        self.OR=organisms
    def nextTurn(self):
        pass
    def drawWorld(self):
        self.Table_of_world=[]
        for i in range(1,21):
            Helping_table=[]
            for j in range(1,21):
                Helping_table.append(0)
            self.Table_of_world.append(Helping_table)

class Organism:
    current_id = 1
    def __init__(self, strenght, initiative, location, world):
        self.id=Organism.current_id
        Organism.current_id += 1
        #self.type=type
        self.strenght=strenght
        self.initiative=initiative
        self.location=location
        self.world=world
    def action(self):
        pass
    def colision(self):
        pass
    def drawing(self,image):
        self.world.blit(image,self.location)