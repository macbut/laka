import random

from main import Organism

class Plant(Organism):
    # def action(self,id):
    #     if random.randint(1,6)==2:
    #         pass
    pass
class Grass(Plant):
    pass

class Guarana(Plant):
    pass

class Berries(Plant):
    pass

trawa1 = Grass(1,1,1,1)
trawa2 = Grass(1,1,1,1)
print(trawa1.id)
print(trawa2.id)