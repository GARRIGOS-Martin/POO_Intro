# On va créer un Zoo virtuel

class Animal():
    

    def __init__(self,poids, taille):
        self.set_poids(poids)
        self.taille = taille
    
    def get_poids(self):
        return self.__poids

    def set_poids(self, poids):
        if poids < 0 :
            raise ValueError
        else : 
            self.__poids = poids
        
    def se_deplacer(self):
        pass

    def __str__(self):
        return "L'animal pèse " +  str(self.get_poids()) + " kg" + " et mesure " + str(self.taille) + " centimètres de hauteur."







  