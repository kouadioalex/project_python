#
# fonction recuperer_et_afficher
# parametre numero_personne
# rien retourner
# variable nom\age

def recuperer_et_afficher(numer_personne):

#--------------------methode 1 --------------------
    """nom = input(f"Nom de la personne {numer_personne}: " )
    age =0
    while age==0:
        ages = input(f"l'age de la personne {numer_personne}: ")
        try:
            age= int(ages)
        except :
            print("erreur, entrez un nombre")

    print(f"la personne N°{numer_personne} nom est: {nom} son age est {age} ans ")

nb = 3
for i in range(nb):
    recuperer_et_afficher(i+1)

"""

#---------------------methode 2--------------------
    """nom = input("entrez le nom " + str(numer_personne) + ":")
    age = input("entrez l'age " +str(numer_personne)+ ":")
    print("la personne n°",numer_personne, "à pour nom ", nom, "son age ", age, "ans ")
recuperer_et_afficher(1)
recuperer_et_afficher(2)
recuperer_et_afficher(3)"""

#
#
#--------------methode 3-----------------------
#------------------<>----------------
def recuperer_info_personne(numer_personne):
    nom_str = input(f"Nom de la personne {numer_personne}: ")
    age_str = input(f"l'age de la personne {numer_personne}: ")
    return nom_str, age_str

def afficher_info_personne(nom, age):

    print(f"la personne "+nom+ " et son âge est: "+ str(age))


#def verifie_age(age):

def recuperer_afficher_info_personne(numer_personne):
    nom, age= recuperer_info_personne(numer_personne)
    afficher_info_personne(nom, age)





nb = 3
for i in range(nb):
    recuperer_afficher_info_personne(i+1)
