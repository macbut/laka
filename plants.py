import random

from main import Organism

class Plant(Organism):
    def action(self,id):
        if random.randint(1,6)==2:
            pass
class Grass(Plant):
    pass

class Guarana(Plant):
    pass

class Berries(Plant):
    pass
