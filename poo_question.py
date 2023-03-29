 # ----class des poser question(herite class base)
# ----objet [stockage des question]
# ----class pour corriger des question(herite class question)

class question:
    def __init__(self,titre, choix, bonne_repone):
        self.titr = titre
        self.choisi = choix
        self.repon = bonne_repone

    def poser_question(self):

        global score
        print('', self.titr)
        for i in range(len(self.choisi)):
            print(i + 1, '-', self.choisi[i])

        print()
        choix_int = question.gestion_erreur(1, len(self.choisi))
        #if choix_v.lower() == reponse.lower() :
        if choix_int ==  self.repon:
            print('bonne reponse !')
            #score += 1
            #print('le score final est:', score)
        else:
            print('mauvaise reponse')
        print()



    def gestion_erreur (min, max):

        choix_str = input(f"entrez la bonne reponse entre ({min} et {max}) : ")
        try:
            choix_int= int(choix_str)
            if min <= choix_int <= max:
                return choix_int
            print(f'erreur, saissir un nombre compris entre {min} et {max} ')
        except:
            print(f"erreur, entrez uniquement que des nombres ")

        #return gestion_erreur(min, max)

class questionnaire: #(question):
    def __init__(self,questions):
        self.quest = questions

    def lancer_question(self):
        score= 0
        for question in self.quest:
            if question.poser_question(question):
                score +=1
        print('le score final est: ', score, 'sur' ,len(self.quest))

resultat = (questionnaire("quelle est la capitale du Ghana ?", ('Sata', 'Noé', 'Accra'), 3),
            questionnaire("quelle est la capitale du Ghana ?", ('Sata', 'Noé', 'Accra'), 2)

            ).lancer_question() 