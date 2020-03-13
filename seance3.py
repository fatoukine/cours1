class animal:
    def __init__(self, type, age, sexe):
        
        self.type = type
        self.age = age
        self.sexe = sexe
        
    def __str__(self):
        return "Cet animal est un(e) " + self.type + " son age " + str(self.age) + " son sexe " + self.sexe

class farm:
    def __init__(self, nom):
        self.animal_list = []
        self.nom = nom
    def __str__(self):
        return "Ceci est " + self.nom  
               
if __name__ == "__main__":

    farm_list = []
    farm_list.append(farm("ma premiere ferme"))
    farm_list[0].animal_list.append(animal("salimata","4","femelle"))
    farm_list[0].animal_list.append(animal("sophie","3","femelle"))
    farm_list[0].animal_list.append(animal("vache","13","femelle"))

    farm_list.append(farm("ma deuxieme ferme"))
    farm_list[1].animal_list.append(animal("mouton","4","femelle"))
    farm_list[1].animal_list.append(animal("mouton","3","femelle"))
    farm_list[1].animal_list.append(animal("vache","13","femelle"))

    farm_list.append(farm("ma troisieme ferme"))
    farm_list[2].animal_list.append(animal("cheval","4","femelle"))
    farm_list[2].animal_list.append(animal("souris","3","femelle"))
    farm_list[2].animal_list.append(animal("chat","13","femelle"))
        
    print(farm_list[0])
    print(farm_list[0].animal_list[0])
    print(farm_list[0].animal_list[1])
    print(farm_list[0].animal_list[2])
    print(farm_list[1])
    print(farm_list[1].animal_list[0])
    print(farm_list[1].animal_list[1])
    print(farm_list[1].animal_list[2])
    print(farm_list[2])
    print(farm_list[2].animal_list[0])
    print(farm_list[2].animal_list[1])
    print(farm_list[2].animal_list[2])

    

