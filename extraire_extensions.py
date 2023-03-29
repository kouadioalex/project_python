#
#
#------------------------------<>---------------------------

def recupere_extension(nom_fichier):
    fichier_split = nom_fichier.split(".")
    if len( fichier_split ) > 1:
        return fichier_split[-1]
    return None

def obtenir_extension(  extension, definition ) :
    for p in definition:
        if p[0].lower() == extension.lower() :
            return p[1]
    return None

fichiers = ("notepad.exe", "nom.fichier.perso.doc", "note.txt", "vacances.jpeg", "planning","date.dat")

definition_extension= [ ("exe", "excutable"),
                        ("doc", "document world"),
                        ("txt", "document texte"),
                        ("JPEG", "image JPEG"),
                        ]

for fiche in fichiers:
    ext = recupere_extension(fiche)
    if ext:
        definition = obtenir_extension( ext, definition_extension )
        if not definition:
            definition = " Extension non connus "
    else:
        definition = "aucun extension"

    print(fiche + "  " +definition + " ")




