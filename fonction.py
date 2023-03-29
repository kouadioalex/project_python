#
#
"""print("bonjour")
nom = input("entrez votre nom: ")
print("votre nom est: "+nom)
"""
#------------------<>----------------
def age_verifie(ages):

    if ages >= 18:
        return True
    return False

def affichage(nom="", age=0):

    if nom=="":
        print("bonjour vous n'avez pas donnez de nom, votre age est ", age)
    else:
        if age==0:
            print("bonjour", nom)
        else:
            print( "bonjour", nom, "son age est:", age , " ans ")

    print("le nombre de caratère est: " ,len(nom) , "caractère")

print("bonjour")
#affichage(age="20")

"""age= 23
if age ==0:
    exit(0)
print("l'age de la personne est ", age, " ans ")
p =age_verifie(age)
if p:
    print("vous etre etre majeur")
else:
    print("vous etre mineur ")
    """

age = 34
# ou
#age_str= input(" entrez votre âge: ")
#age = int(age_str)

if age!=0:
    #exit(0)
    print("l'age de la personne est ", age, " ans ")
    p =age_verifie(age)
    if p:
        print("vous etre etre majeur")
    else:
        print("vous etre mineur ")

