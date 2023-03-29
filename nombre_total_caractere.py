#
#
#
"""def nombre_caractere():
    soms = 0
    for i in nom:
        soms += len(i)
    print("le nombre total est = ", soms)

nom= ('bah', 'alex', 'alice', 'jean', "maire", "nogues")

nombre_caractere()"""


nom = []


def nom_et_somme():
    som= 0
    for i in nom:
        som += len(i)
    print(som)

nb = 3
for p in range(nb):
    entre = input(" entrez votre nom : ")
    nom.append(entre)
print(nom)
nom_et_somme()



