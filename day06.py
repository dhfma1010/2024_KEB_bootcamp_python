class Pokemon:
    def __init__(self,name):
        self.__name = name

p1 = Pokemon("Bulbasaur")

p2 = Pokemon("Ivysaur")

p1.categoty = "seed"
p1.name = "Bulbasaur"
p1.type = "grass"

p1.evolusion = p2

print(p1.evolusion)



