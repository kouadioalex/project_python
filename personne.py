#
#
#
#
def info_prof():
    age_int=0
    while age_int==0:
        age= input("entre votre age : ")
        try:
            age_int= int(age)
        except:
            print("erreur entrez un nombre")
    print(f"votrez est {age_int} ans")


def professeur ():
    nom = input("entrez votre nom: ")
    print("bonjour Mr ", nom)
    print("voulez-vous postuler pour etre prof de math ou anglais")
    noms= input("entrez anglais ou math ")
    if noms== "math":
        print("bravo")
        info_prof()
    else:
        print("vous prof anglais")

def personne(p):
    if p.lower() == "prof":
        professeur()
        print(" bonjour professeur ")
    else:
        print(" bonjour etudiant")
        eleve()

def eleve():
    nom_elev =""
    while not nom_elev =="":
        nom_ele = input(' entrez votre nom: ')
        try:
            nom_elev = nom_ele
        except:
            print("erreur, entrez des lettres et non vide")

    print(f"votre nom est {nom_elev}")





choix = input("votre profesion: ")

personne(choix )

