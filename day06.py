class Animal:
    def says(self):
        return "I Speak"

class Horse(Animal):
    def says(self):
        return

class Donkey(Animal):

    pass

class Mule(Donkey, Horse):
    pass
class Hinny(Horse, Donkey):
    pass