textclass animal:
    def __init__(self, nom, nourriture, nombre=0):
        
        self.nom = nom
        self.nombre = nombre
        self.nourriture = nourriture
        
    def __str__(self):
        return "Cet animal est un " + self.nom + " qui mange " + self.nourriture + " il y en a " + str(self.nombre) + " dans le zoo"
        

class mammifere(animal) :
    
    def __init__(self, nom, nourriture, regime_alimentaire, nbr_pattes=0, nombre=0):
        
        self.nom = nom
        self.nombre = nombre
        self.nourriture = nourriture
        self.regime_alimentaire = regime_alimentaire
        self.nbr_pattes = nbr_pattes
        
    def __str__(self):
        
        return "Cet animal est un " + self.nom + " qui mange " + self.nourriture + " il y en a " + str(self.nombre) + " dans le zoo" + " il est un " + self.regime_alimentaire + " et a " + str(self.nbr_pattes) + " pattes"    



class domestique(animal) :
    
    def __init__(self, nom, nourriture, regime_alimentaire, nbr_pattes=0, nombre=0):
        
        self.nom = nom
        self.nombre = nombre
        self.nourriture = nourriture
        self.regime_alimentaire = regime_alimentaire
        self.nbr_pattes = nbr_pattes
        
    def __str__(self):
        
        return "Cet animal domestique est un " + self.nom + " qui mange " + self.nourriture + " il y en a " + str(self.nombre) + " dans le zoo" + " il est un " + self.regime_alimentaire + " et a " + str(self.nbr_pattes) + " pattes"    
 

class animal_marin(animal) :
    
     pass

if __name__ == "__main__":
    zoo = {}
    zoo["mammifere1"] = mammifere("humain","600g","omnivore",2 ,2)
    zoo["mammifere2"] = mammifere("lion","3kg","carnivore",1 ,4)
    zoo["mammifere3"] = mammifere("lapin","100g","vegetarien",7 ,4)
    zoo["mammifere4"] = mammifere("mouton","500g","vegetarien",5 ,4)
    zoo["mammifere5"] = mammifere("chien","3g","omnivore",2 ,4)
    zoo["domestique1"] = domestique("lapin","100g","vegetarien",7 ,4)
    zoo["domestique2"] = domestique("mouton","3g","vegetarien",5 ,4)
    zoo["domestique3"] = domestique("chien","3g","omnivore",2 ,4)
    zoo["domestique4"] = domestique("poule","200g","omnivore",8 ,2)
    zoo["marin"] = animal_marin("pieuvre","200g",1)

    for my_key in zoo:
        
        print(my_key + " " + str(zoo[my_key]))
    print (len(zoo))
    print("nbr de nourriture par semainne est de ")
    m= (600+3000+100+500+500+200+1000+200+1000+200000)*7 
    print(m)
    print("le nombre de pattes est de")
    p= (2+4+4+4+4+4+4+4+2)
    print(p)
    omni = 1
    if self.regime_alimentaire = "omnivore"
        omni = omni +1
        print(omni)
    
