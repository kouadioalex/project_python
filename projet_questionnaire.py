#
#
#
#---------------------simple ---------------------

"""print("Question ")
def question1(b):

    print("quelle est la capitale du Burkina Faso?")
    print("a- Korogho")
    print(f"{b}-Ouagadougou ")
    print("c- Accra")
    reponse(b)

def question2(c):

    print("quelle est la capitale du Mali ?")
    print("a- Nyame")
    print("b- Conagri")
    print(f"{c}- Accra")
    reponse2(c)

def question3(c):
    print("quel la capitale du Ghana ?")
    print("a- Nyame")
    print("b- Conagri")
    print(f"{c}- Accra")
    print()


def question4(a):
    print("quelle est la capitale de la cote d'ivoire ?")
    print(f"{a}- Abidjan")
    print("b- Bouaké")
    print("c- daloa")

def reponse(b):

    choix = input("votre reponse est:  ?")
    if choix==b:
        print("bonne reponse")
    else:
        print("faux")

def reponse2(c):
    choix = input("votre reponse est:  ?")
    if choix == c:
        print("bonne reponse")
    else:
        print("faux")

question1( "b" )
question2("c")
#reponse("")
"""
##############---------------------avec fonction factoriser-----------------
def poser_question(question, r1,r2,r3, choix):

    global score
    print("Question:")
    print(" ",question)
    print("  a-",r1)
    print("  b-",r2)
    print("  c-",r3)

    reponse = input("entrez votre reponse: ")
    if reponse==choix:
        print("Bonne reponse ")
        score += 1
    else:
        print("Mauvaise reponse")

score =0
poser_question("quelle est la capitale du Burkina Faso ?  ","Korogho", "Ouagadougou ", "Accra", "b" )
print()
poser_question("quelle est la capitale de la cote d'ivoire ?  ","Bouaké", "Yamoussokro ", "Abidjan", "c"  )
print()
poser_question("quelle est la capitale du Mali ?  ","Bamako", "djanklo ", "Daloa", "a"  )
print()
poser_question("quelle est la capitale du Ghana ?  ","Bobo Dioulaso", "Man ", "Accra", "c"  )
print()
print("le score final est: ",score)
