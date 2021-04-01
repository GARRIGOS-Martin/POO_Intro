from Animal import *

# Je crée la classe Oiseau
class Oiseau(Animal):
    is_Oiseau = True

    def se_deplacer(self):
        print("Je vole")

    def __init__(self, poids, taille, altitude_max):
        super().__init__(poids, taille)
        self.altitude_max = altitude_max
        
corbeau = Oiseau(5, 35, 200)
print(corbeau.get_poids(), corbeau.taille, corbeau.altitude_max)


