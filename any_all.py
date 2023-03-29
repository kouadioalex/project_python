#
#
"""noms= ["bah", "alexandre", "alice", "jean", "marie", "nogues"]
#print(any(noms))

nom_existe= all(True if "a" in nom.lower() else False for nom in noms)
if nom_existe:
    print("trouvé")
else:
    print("faux")"""

def chaine_caractere(chaine):
    return any( [ c.isdigit() for  c in chaine ])
    """for c in chaine:
        if c.isdigit():
            return True
        return False"""

nom = input("entrez le nom : ")
if nom==" ":
    print(" votre nom est vide ")
elif chaine_caractere(nom):
    print("ce nom est invalide, il contient des chiffre ")
else:
    print("bonjour " + nom)

"""nom= "toto34"
noms= any(i.isdigit() for i in nom)
print(noms)"""






