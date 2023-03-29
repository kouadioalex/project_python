#
#
#-----------------slice---------------

"""noms= ["bah", "alexandre", "alice", "jean", "maire", "nogues"]
silce_nom = noms
noms[1]=   "toto"

print(silce_nom)
print(noms)"""


#
#
"""print("1", r1)
print("a" ,r2)
print("b",r3)
print("c-",r4)"""

#def questionnaire(r1, r2, r3, r4, reponse):
def poser_question(question):

    titre_question= question[0]
    choix= question[1]
    bonne_reponse= question[2]

    print(titre_question)
    for i in choix:
        print("a", i)

    reponse= input("votre reponse :")
    if reponse== bonne_reponse:
        print("bonne reponse")
    else:
        print("mauvaise reponse ")




def lancer_question(questionnaire):
    for question in questionnaire:
        poser_question(question)

questionnaire=(
    ("quelle est la capitale de la Côte d'ivoire" , ("yakro", "abidjan", "bouaké"), "abidjan"),
    ("quelle est la capitale du Burkina" , ("conakri", "abidjan", "bouaké"), "conakri"),
    ("quelle est la capitale du Mali" , ("yakro", "bamako", "bouaké", "nissa","tiassa"), " bamako"),
    ("quelle est la capitale du Ghana" , ("yakro", "abidjan", "accra"), "accra") )

lancer_question(questionnaire)


