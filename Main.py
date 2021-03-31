from ZOO import *

# Instanciation de nos objets 
chat = Animal(4,50)
corbeau = Oiseau(5, 35, 200)
python = Serpent(1, 2)
boa = Serpent(2, 6)
carpe = Animal(6, 80)
requin = Animal(60, 210)
pelican = Animal(1, 25)

#On peut visualiser notre string retourné qui définit plus explicitement notre objet
ani = Animal(5,30)
print(str(ani))



# Afin de concaténer les deux objets de type Zoo, je crée z1 et z2.
Ferme = [chat, corbeau, python]
ferme = Zoo(Ferme)

#Je teste la fonction que l'on a créée pour ajouter un animal dans notre objet de type Zoo
ferme.ajoute_animal()

Poissons = [carpe, requin, pelican]
poissons = Zoo(Poissons)

#Ici on pourra visualiser le contenu de z3
print(ferme + poissons)



