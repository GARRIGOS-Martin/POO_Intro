from Animal import *
class Zoo():

    def __init__(self, liste):
        for elt in liste :
            if isinstance(elt, Animal) == False :
                raise ValueError
        self.liste = liste

    def ajoute_animal(self, animal):
        if isinstance(animal, Animal):
            self.liste.append(animal)
    
    def __str__(self):
        lst = ""
        for animal in self.liste :
            lst += str(animal) + "\n"
        return "Mon zoo est composé de : " + str(lst)


    def __add__(self, autre):
        if isinstance(autre, Zoo):
            z3 = self.liste + autre.liste
            return Zoo(z3)
        else : 
            raise TypeError
        