
#
#print
#demande lui de rentrez un nombre obligatoire

#------------------<>----------------
def affichage(nom, age):
    print()
    print("votre nom est: ", nom)
    print(f"son age est :{age} ans")
    #print(f"votre age prochain est: {proch}")


def verifie(age):
    if age >= 18:
        print("vous etre majeur")
    else:
        print("vous etre mineur")

def personne(numbpers):
    nom = input(f"entrez votre nom{numbpers} : ")

    age = 0
    while age == 0:
        ages = input(f"entrez votre age{numbpers} : ")
        try:
            age = int(ages)
            #proch = (age + 1)
        except:
            print("erreur, entrez un nombre")

    affichage(nom, ages)
    verifie(age)
    print()
    return True

nmbre =0
p= 3
for i in  range(1, p):
    if personne(i):
        nmbre +=1
print(f" le nombre est {nmbre} personne")

"""""nmbre_nim = 1
nmbre_max = 10

nb=0
def nombre_magique():

    nb_magic= input("entrez le nombre magique:")
    if nb_magic== 4:
        print("bravoo !")

    else:
        print("desolé")

nombre_magique()
"""""