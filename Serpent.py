from Animal import *
# Je crée la classe Serpent 
class Serpent(Animal):
    is_Serpent = True

    def se_deplacer(self):
        print("Je rampe")

python = Serpent(1, 2)
