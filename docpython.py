def lecture_des_fichiers():
    fichier = open("document.txt", "r")
    print(fichier.read())
    return

def ecriture_des_fichiers():
    fichier = open("document.txt", "a")
    fichier.write("c'est cooOOOOOL")

if __name__ == "__main__":

    lecture_des_fichiers()
    ecriture_des_fichiers()
