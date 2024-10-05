class Monika():
    def __init__(self,wiek):
        self.wiek=wiek

gatunek1="lew"
tab1=[]
for i in range(1,10):
    gatunek1 = Monika(i)
    tab1.append(gatunek1)

for i in tab1:
    if i.wiek == 3:
        print(i.wiek)