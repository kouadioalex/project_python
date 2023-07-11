
import tkinter
import tkinter.constants
#from PIL import  Image, ImageTk
from  tkinter import ttk
from  tkinter import ttk
from email.mime import image
from tkinter import *
from tkinter.messagebox import  showerror, showinfo, showwarning
app= Tk()
app.title('mon application ecole                developpeur: kouadio bah  (CI:+225 0758822279 )')
#app.geometry("600x600")
app.config(bg="gray30")
app.iconbitmap()
btnEtat= False

couleur={"nero": "#252726",
         "purple": "#800080",
         "white": "#FFFFFF"}
#
#-------------- definition de la fonctione swhich--------
def switch():
    global btnEtat
    if  btnEtat is True:
        for x in range(400):
            page.place(x=-x, y=0)
            topFrame.update()

        #------ reste couleur widgets---------
        bannerText.config(fg="purple")
        accueilText.config(bg=couleur["purple"])
        topFrame.config(bg=couleur["purple"])
        app.config(bg="gray30")
        btnEtat= False

    else:
        for x in range(-300, 0):
            page.place(x=x, y=0)
            topFrame.update()
            btnEtat=True




#--------------------------text de top var------------------
topFrame= tkinter.Frame(app, bg=couleur["purple"])
topFrame.pack(side="top", fill=tkinter.X)

accueilText= tkinter.Label(topFrame, text="BAH", font='ExtraCondensed 15'
                           ,bg=couleur["nero"], fg="white", height=2,  padx=20)

accueilText.pack(side='right')
can = Canvas(app, width=700, height=600)

fontimag= PhotoImage(  file='imagecole/fleure.png')
can.create_image(0, 0, anchor=NW, image=fontimag)


bannerText= tkinter.Label(app, text="Text de Developpement \nWeb",
                          font='ExtraCondensed 15',
                          fg="purple" )
bannerText.place(x=100, y=550)
can.pack(side='left')


#-----------------------la page du bouton menus------------

page= tkinter.Frame(app, bg='gray30', width=400, height=600)
#page.pack(side='top')
tkinter.Label(page, font="ExtraCondensed 15", bg=couleur["purple"],
               fg='black', width=300, height=2, padx=20).place( x=0, y=0 )
y= 55

#=========================l'icon du menus=================
NavIcon= PhotoImage(file="imagecole/menus1.png", width=30 ,height=30)
navmenu= tkinter.Button(topFrame, image=NavIcon, bg=couleur["white"],
                        padx=10, activebackground=couleur["nero"],
                        command=switch )
navmenu.place(x=10, y=5)

#================parametrer le bouton fermerture======================

close= PhotoImage(file="imagecole/fermer1.png", width=20, height=20)
ferme= tkinter.Button(page, bg=couleur["white"],image=close,
                      activebackground=couleur["purple"], bd=0, command=switch )
ferme.place(x=370, y=55)

#===================les elements de la page======================

option= ["ACCUEIL", "PAGES", "PROFIL", "PARAMETRES", "AIDE"]

#==================parametrage du BOUTON ACCUEIL===================

pageAccueil= tkinter.Frame(app, bg='blue', width=600, height=600)


topFrame1= tkinter.Frame(pageAccueil, bg='red', width=600, height=600 )
topFrame2= tkinter.Frame(pageAccueil, bg='gray30', width=600, height=600 )
topFrame3= tkinter.Frame(pageAccueil, bg='yellow', width=600, height=600 )
topFrame4= tkinter.Frame(pageAccueil, bg='gray30', width=600, height=600 )
topFrame5= tkinter.Frame(pageAccueil, bg='yellow', width=600, height=600 )
topFrame6= tkinter.Frame(pageAccueil, bg='gray30', width=600, height=600 )
topFrame7= tkinter.Frame(pageAccueil, bg='yellow', width=600, height=600 )
#topFrame8= tkinter.Frame(pageAccueil, bg='gray30', width=600, height=600 )
#topFrame9= tkinter.Frame(pageAccueil, bg='yellow', width=600, height=600 )
#topFrame1.pack(side='left', fill=tkinter.X)
#topFrame1.place(x=0, y=200)

#================liste inscrit en 6ième========


def inscrit_sixieme():
    # ======ouverture du page================
    for x in range(-300, 0):
        topFrame1.place(x=x, y=40)
        #for x in range(700):
        topFrame2.place(x=-700 )
        topFrame3.place(x=-700 )
        topFrame4.place(x=-700 )
        topFrame5.place(x=-700 )
        topFrame6.place(x=-700 )
        topFrame7.place(x=-700 )

    global listeper
    nom = Label(topFrame1, text="Nom ", font="Helvetica 14 bold", bg='red', bd=5)
    prenom = Label(topFrame1, text="Prenom ", font="Helvetica 14 bold", bg='red', bd=5)
    teleph = Label(topFrame1, text="Telephone ", font="Helvetica 14 bold", bg='red', bd=5)
    matricul = Label(topFrame1, text="Matricule ", font="Arial 14 bold", bg='red', bd=5)
    clas = Label(topFrame1, text="Classe ", font="Times 14 bold", bg='red', bd=5)

    nom.place(x=30, y=20)
    prenom.place(x=100, y=20)
    teleph.place(x=200, y=20)
    matricul.place(x=325, y=20)
    clas.place(x=440, y=20)

    if listeElevesix:
        y= 60
        for S in listeElevesix:
            nmss= Label(topFrame1, text=S.nm )
            prenss= Label(topFrame1, text=S.prenm )
            teless=Label(topFrame1, text=S.teleph )
            matrss= Label(topFrame1, text=S.matr )
            clases= Label(topFrame1, text=S.clas )

            nmss.place(x=30, y=y)
            prenss.place(x=100, y=y)
            teless.place(x=200, y=y)
            matrss.place(x=325, y=y)
            clases.place(x=440, y=y)

            y+=30


def inscrit_cinquieme():
    for x in range(-300, 0):
        topFrame2.place(x=x, y=40)
        #for x in range(700):
        topFrame1.place(x=-700, )
        topFrame3.place(x=-700, )
        topFrame4.place(x=-700)
        topFrame5.place(x=-700)
        topFrame6.place(x=-700)
        topFrame7.place(x=-700)

    global listeper

    nom = Label(topFrame2, text="Nom ", font="Helvetica 14 bold", bg='red', bd=5)
    prenom = Label(topFrame2, text="Prenom ", font="Helvetica 14 bold", bg='red', bd=5)
    teleph = Label(topFrame2, text="Telephone ", font="Helvetica 14 bold", bg='red', bd=5)
    matricul = Label(topFrame2, text="Matricule ", font="Arial 14 bold", bg='red', bd=5)
    clas = Label(topFrame2, text="Classe ", font="Times 14 bold", bg='red', bd=5)

    nom.place(x=30, y=20)
    prenom.place(x=100, y=20)
    teleph.place(x=200, y=20)
    matricul.place(x=325, y=20)
    clas.place(x=440, y=20)

    if listeElevecinq:
        y= 60
        for C in listeElevecinq:
            nms= Label(topFrame2, text=C.nm )
            prens= Label(topFrame2, text=C.prenm )
            teles=Label(topFrame2, text=C.teleph )
            matrs= Label(topFrame2, text=C.matr )
            clase= Label(topFrame2, text=C.clas )

            nms.place(x=30, y=y)
            prens.place(x=100, y=y)
            teles.place(x=200, y=y)
            matrs.place(x=325, y=y)
            clase.place(x=440, y=y)

            y+=30

def inscrit_quatrieme():
    #======ouverture du page================
    for x in range(-300, 0):
        topFrame3.place(x=x, y=40)
        #for x in range(700):
        topFrame1.place(x=-700, )
        topFrame2.place(x=-700,)
        topFrame4.place(x=-700)
        topFrame5.place(x=-700)
        topFrame6.place(x=-700)
        topFrame7.place(x=-700)



    global listeper
    nom= Label(topFrame3, text="Nom ", font ="Helvetica 14 bold", bg='red', bd=5)
    prenom= Label(topFrame3, text="Prenom ", font ="Helvetica 14 bold", bg='red', bd=5)
    teleph= Label(topFrame3, text="Telephone ", font ="Helvetica 14 bold", bg='red', bd=5)
    matricul= Label(topFrame3, text="Matricule ", font ="Arial 14 bold", bg='red', bd=5)
    clas= Label(topFrame3, text="Classe ", font ="Times 14 bold", bg='red', bd=5)

    nom.place(x=30, y=20)
    prenom.place(x=100, y=20)
    teleph.place(x=200, y=20)
    matricul.place(x=325, y=20)
    clas.place(x=440, y=20)

    if listeElevequatr:
        y= 60
        for p in listeElevequatr:
            nms= Label(topFrame3, text=p.nm )
            prens= Label(topFrame3, text=p.prenm )
            teles=Label(topFrame3, text=p.teleph )
            matrs= Label(topFrame3, text=p.matr )
            clase= Label(topFrame3, text=p.clas )

            nms.place(x=30, y=y)
            prens.place(x=100, y=y)
            teles.place(x=200, y=y)
            matrs.place(x=325, y=y)
            clase.place(x=440, y=y)

            y+=30

def inscrit_troixieme():
    #======ouverture du page================
    for x in range(-300, 0):
        topFrame4.place(x=x, y=40)

        topFrame1.place(x=-700, )
        topFrame2.place(x=-700,)
        topFrame3.place(x=-700)
        topFrame5.place(x=-700)
        topFrame6.place(x=-700)
        topFrame7.place(x=-700)



    global listeper
    nom= Label(topFrame4, text="Nom ", font ="Helvetica 14 bold", bg='red', bd=5)
    prenom= Label(topFrame4, text="Prenom ", font ="Helvetica 14 bold", bg='red', bd=5)
    teleph= Label(topFrame4, text="Telephone ", font ="Helvetica 14 bold", bg='red', bd=5)
    matricul= Label(topFrame4, text="Matricule ", font ="Arial 14 bold", bg='red', bd=5)
    clas= Label(topFrame4, text="Classe ", font ="Times 14 bold", bg='red', bd=5)

    nom.place(x=30, y=20)
    prenom.place(x=100, y=20)
    teleph.place(x=200, y=20)
    matricul.place(x=325, y=20)
    clas.place(x=440, y=20)

    if listeElevetroix:
        y= 60
        for p in listeElevetroix:
            nms= Label(topFrame4, text=p.nm )
            prens= Label(topFrame4, text=p.prenm )
            teles=Label(topFrame4, text=p.teleph )
            matrs= Label(topFrame4, text=p.matr )
            clase= Label(topFrame4, text=p.clas )

            nms.place(x=30, y=y)
            prens.place(x=100, y=y)
            teles.place(x=200, y=y)
            matrs.place(x=325, y=y)
            clase.place(x=440, y=y)

            y+=30

def inscrit_second():
    #======ouverture du page================
    for x in range(-300, 0):
        topFrame5.place(x=x, y=40)
        #for x in range(700):
        topFrame1.place(x=-700, )
        topFrame2.place(x=-700,)

        topFrame4.place(x=-700)
        topFrame3.place(x=-700)
        topFrame6.place(x=-700)
        topFrame7.place(x=-700)



    global listeper
    nom= Label(topFrame5, text="Nom ", font ="Helvetica 14 bold", bg='red', bd=5)
    prenom= Label(topFrame5, text="Prenom ", font ="Helvetica 14 bold", bg='red', bd=5)
    teleph= Label(topFrame5, text="Telephone ", font ="Helvetica 14 bold", bg='red', bd=5)
    matricul= Label(topFrame5, text="Matricule ", font ="Arial 14 bold", bg='red', bd=5)
    clas= Label(topFrame5, text="Classe ", font ="Times 14 bold", bg='red', bd=5)

    nom.place(x=30, y=20)
    prenom.place(x=100, y=20)
    teleph.place(x=200, y=20)
    matricul.place(x=325, y=20)
    clas.place(x=440, y=20)

    if listeElevesecond:
        y= 60
        for p in listeElevesecond:
            nms= Label(topFrame5, text=p.nm )
            prens= Label(topFrame5, text=p.prenm )
            teles=Label(topFrame5, text=p.teleph )
            matrs= Label(topFrame5, text=p.matr )
            clase= Label(topFrame5, text=p.clas )

            nms.place(x=30, y=y)
            prens.place(x=100, y=y)
            teles.place(x=200, y=y)
            matrs.place(x=325, y=y)
            clase.place(x=440, y=y)

            y+=30

def inscrit_premieme():
    #======ouverture du page================
    for x in range(-300, 0):
        topFrame6.place(x=x, y=40)
        #for x in range(700):
        topFrame1.place(x=-700, )
        topFrame2.place(x=-700,)
        topFrame3.place(x=-700)
        topFrame4.place(x=-700)
        topFrame5.place(x=-700)
        topFrame7.place(x=-700)



    global listeper
    nom= Label(topFrame6, text="Nom ", font ="Helvetica 14 bold", bg='red', bd=5)
    prenom= Label(topFrame6, text="Prenom ", font ="Helvetica 14 bold", bg='red', bd=5)
    teleph= Label(topFrame6, text="Telephone ", font ="Helvetica 14 bold", bg='red', bd=5)
    matricul= Label(topFrame6, text="Matricule ", font ="Arial 14 bold", bg='red', bd=5)
    clas= Label(topFrame6, text="Classe ", font ="Times 14 bold", bg='red', bd=5)

    nom.place(x=30, y=20)
    prenom.place(x=100, y=20)
    teleph.place(x=200, y=20)
    matricul.place(x=325, y=20)
    clas.place(x=440, y=20)

    if listeElevepremiem:
        y= 60
        for p in listeElevepremiem:
            nms= Label(topFrame6, text=p.nm )
            prens= Label(topFrame6, text=p.prenm )
            teles=Label(topFrame6, text=p.teleph )
            matrs= Label(topFrame6, text=p.matr )
            clase= Label(topFrame6, text=p.clas )

            nms.place(x=30, y=y)
            prens.place(x=100, y=y)
            teles.place(x=200, y=y)
            matrs.place(x=325, y=y)
            clase.place(x=440, y=y)

            y+=30

def inscrit_terminal():
    #======ouverture du page================
    for x in range(-300, 0):
        topFrame7.place(x=x, y=40)
        #for x in range(700):
        topFrame1.place(x=-700, )
        topFrame2.place(x=-700,)
        topFrame4.place(x=-700)
        topFrame5.place(x=-700)
        topFrame6.place(x=-700)
        topFrame3.place(x=-700)



    global listeper
    nom= Label(topFrame7, text="Nom ", font ="Helvetica 14 bold", bg='red', bd=5)
    prenom= Label(topFrame7, text="Prenom ", font ="Helvetica 14 bold", bg='red', bd=5)
    teleph= Label(topFrame7, text="Telephone ", font ="Helvetica 14 bold", bg='red', bd=5)
    matricul= Label(topFrame7, text="Matricule ", font ="Arial 14 bold", bg='red', bd=5)
    clas= Label(topFrame7, text="Classe ", font ="Times 14 bold", bg='red', bd=5)

    nom.place(x=30, y=20)
    prenom.place(x=100, y=20)
    teleph.place(x=200, y=20)
    matricul.place(x=325, y=20)
    clas.place(x=440, y=20)

    if listeEleveterminal:
        y= 60
        for t in listeEleveterminal:
            nms= Label(topFrame7, text=t.nm )
            prens= Label(topFrame7, text=t.prenm )
            teles=Label(topFrame7, text=t.teleph )
            matrs= Label(topFrame7, text=t.matr )
            clase= Label(topFrame7, text=t.clas )

            nms.place(x=30, y=y)
            prens.place(x=100, y=y)
            teles.place(x=200, y=y)
            matrs.place(x=325, y=y)
            clase.place(x=440, y=y)

            y+=30


def ferm():
    for x in range( 700):
        topFrame1.place(x=-x, y=y)

def ferm2():
    for x in range( 700):
        topFrame2.place(x=-x, y=y)

def ferm3():
    for x in range( 700):
        topFrame3.place(x=-x, y=y)



#===============bouton deroulant des differents classes ================

#listeaccueill= ['6ièm', '5ièm', '4ièm', '3ièm', '2nd', '1er', 'BAC' ]
liste_niveau= tkinter.Frame(app,  width=599, height=40, bg='green' )

bout_sixieme=Button(liste_niveau, text='6ièm', command= inscrit_sixieme )
bout_sixieme.place(x=20, y=10)

bout_cinqieme=Button(liste_niveau, text='5ièm', command= inscrit_cinquieme )
bout_cinqieme.place(x=70, y=10)

bout_quatrieme=Button(liste_niveau, text='4ièm', command= inscrit_quatrieme )
bout_quatrieme.place(x=120, y=10)

bout_=Button(liste_niveau, text='3ièm ', command= inscrit_troixieme )
bout_.place(x=170, y=10)

bout_=Button(liste_niveau, text='2nd ', command= inscrit_second )
bout_.place(x=220, y=10)

bout_=Button(liste_niveau, text='1ier ', command= inscrit_premieme )
bout_.place(x=270, y=10)

bout_=Button(liste_niveau, text='Tle ', command= inscrit_terminal )
bout_.place(x=320, y=10)

#bout_=Button(liste_niveau, text=' ', command= '' )
#bout_.place(x=350, y=10)

def niveau_class():
    for x in range(-300, 0):
        liste_niveau.place(x=0, y=55)

def clasferm():
    for x in range(650):
        liste_niveau.place(x=-x, y=y)
        topFrame1.place(x=-700)
        topFrame2.place(x=-700)
        topFrame3.place(x=-700)
        topFrame4.place(x=-700)
        topFrame5.place(x=-700)
        topFrame6.place(x=-700)
        topFrame7.place(x=-700)


lite= tkinter.Button(pageAccueil, text='liste des classes', command=niveau_class )
lite.place(x=250, y=10,)

clasfer= Button(liste_niveau, image=close, bg=couleur["white"],
                          activebackground=couleur["purple"], bd=0, command=clasferm )
clasfer.place(x=570, y=2)


#baraccueil= Label(pageAccueil, bd=20, width=75, relief= RIDGE,   text="liste des éleves inscrits",  )
#baraccueil.place(x=10, y=130)


        #==============ouverture de la page ======================
def acc():
    for x in range(-300, 0):
        pageAccueil.place(x=x, y=y)

        #==========fermeture de la page===================
def accferm():
    for x in range(650):
        pageAccueil.place(x=-x, y=y)
        liste_niveau.place(x=-x, y=y)





fermeaid = tkinter.Button(pageAccueil, image=close, bg=couleur["white"],
                          activebackground=couleur["purple"], bd=0, command=accferm )
fermeaid.place(x=570, y=10)

#==================parametrage du BOUTON PAGE======================

pagePage= tkinter.Frame(app, bg='yellow', width=600, height=600 )


titre= Label(pagePage, text='la Page', relief=RIDGE, bd=5, width=75, height=2)
titre.place(x=10, y=10)

#========================les differents actions de l'inscriptions des éleves==================

class Eleve:
    def __init__(self, nom, prenom, telephone, matricule, classe):
        self.nm = nom
        self.prenm= prenom
        self.teleph= telephone
        self.matr= matricule
        self.clas= classe

    def __eq__(self, other):
        return (self.nm== other.nm and self.prenm == other.prenm and self.teleph == other.teleph and self.matr == other.matr and self.clas == other.clas )

def appartient(liste, val):
    for i in range(len(liste)):
        if liste[i].__eq__(val):
            return 1
    return 0

def valid():

    global listeElevesix,listeElevecinq,listeElevequatr
    if (nomEntr.get() and prenomEntr.get() and telephoneEntr.get() and matriculEntr.get() and classeEntr.get()):
        if classeEntr.get() == liste1[0]:
            pn=Eleve(nomEntr.get() , prenomEntr.get() , telephoneEntr.get() , matriculEntr.get() , classeEntr.get())
            if appartient(listeElevesix, pn):
                showerror(title='Erreur', message='il existe deja inscrit')
            else:
                listeElevesix.append(pn)
                showinfo(title='Valider', message='{} à été bien enregistrer'.format(prenomEntr.get()) )

        if classeEntr.get() == liste1[1]:
            pn = Eleve(nomEntr.get(), prenomEntr.get(), telephoneEntr.get(), matriculEntr.get(), classeEntr.get())
            if appartient(listeElevecinq, pn):
                showerror(title='Erreur', message='il existe deja inscrit')
            else:
                listeElevecinq.append(pn)
                showinfo(title='Valider', message='{} à été bien enregistrer'.format(prenomEntr.get()))

        if classeEntr.get() == liste1[2]:
            pn = Eleve(nomEntr.get(), prenomEntr.get(), telephoneEntr.get(), matriculEntr.get(), classeEntr.get())
            if appartient(listeElevequatr, pn):
                showerror(title='Erreur', message='il existe deja inscrit')
            else:
                listeElevequatr.append(pn)
                showinfo(title='Valider', message='{} à été bien enregistrer'.format(prenomEntr.get()))

        if classeEntr.get() == liste1[3]:
            pn = Eleve(nomEntr.get(), prenomEntr.get(), telephoneEntr.get(), matriculEntr.get(), classeEntr.get())
            if appartient(listeElevetroix, pn):
                showerror(title='Erreur', message='il existe deja inscrit')
            else:
                listeElevetroix.append(pn)
                showinfo(title='Valider', message='{} à été bien enregistrer'.format(prenomEntr.get()))

        if classeEntr.get() == liste1[4]:
            pn = Eleve(nomEntr.get(), prenomEntr.get(), telephoneEntr.get(), matriculEntr.get(), classeEntr.get())
            if appartient(listeElevesecond, pn):
                showerror(title='Erreur', message='il existe deja inscrit')
            else:
                listeElevesecond.append(pn)
                showinfo(title='Valider', message='{} à été bien enregistrer'.format(prenomEntr.get()))

        if classeEntr.get() == liste1[5]:
            pn = Eleve(nomEntr.get(), prenomEntr.get(), telephoneEntr.get(), matriculEntr.get(), classeEntr.get())
            if appartient(listeElevepremiem, pn):
                showerror(title='Erreur', message='il existe deja inscrit')
            else:
                listeElevepremiem.append(pn)
                showinfo(title='Valider', message='{} à été bien enregistrer'.format(prenomEntr.get()))

        if classeEntr.get() == liste1[6]:
            pn = Eleve(nomEntr.get(), prenomEntr.get(), telephoneEntr.get(), matriculEntr.get(), classeEntr.get())
            if appartient(listeEleveterminal, pn):
                showerror(title='Erreur', message='il existe deja inscrit')
            else:
                listeEleveterminal.append(pn)
                showinfo(title='Valider', message='{} à été bien enregistrer'.format(prenomEntr.get()))

        nomEntr.delete(0, END)
        prenomEntr.delete(0, END)
        telephoneEntr.delete(0, END)
        matriculEntr.delete(0, END)
        classeEntr.delete(0, END)

    else:
        showwarning(title='Erreur', message='renseigner tous les chants' )

def reint():
    nomEntr.delete(0, END)
    prenomEntr.delete(0, END)
    telephoneEntr.delete(0, END)
    matriculEntr.delete(0, END)
    classeEntr.delete(0, END)


imageName, listeElevesix='', list()
imageName, listeElevecinq='', list()
imageName, listeElevequatr='', list()
imageName, listeElevetroix='', list()
imageName, listeElevesecond='', list()
imageName, listeElevepremiem='', list()
imageName, listeEleveterminal='', list()




nom= Label(pagePage, text="Nom ", bd=3, relief=RIDGE, width=10, height=2 )
prenom= Label(pagePage, text="Prenom ", bd=3, relief=RIDGE, width=10, height=2 )
telephone= Label(pagePage, text="Telephone  ", bd=3, relief=RIDGE, width=10, height=2 )
matricul= Label(pagePage, text="Matricule ", bd=3, relief=RIDGE, width=10, height=2 )
classe= Label(pagePage, text="Classe ", bd=3, relief=RIDGE, width=10, height=2 )

nom.place(x=10, y=100)
prenom.place(x=10, y=150)
telephone.place(x=10, y=200)
matricul.place(x=10, y=250)
classe.place(x=10, y=300)

nomEntr= Entry(pagePage, bd=10, relief=RIDGE  )
prenomEntr= Entry(pagePage, bd=10, relief=RIDGE )
telephoneEntr= Entry(pagePage,  bd=10, relief=RIDGE )
matriculEntr= Entry(pagePage,  bd=10, relief=RIDGE )

liste1= ['6ièm', '5iem', '4ièm', '3ièm', '2nd', '1er', 'BAC' ]
classeEntr= ttk.Combobox(pagePage, values=liste1 , state='readonly')

nomEntr.place(x=120, y=100)
prenomEntr.place(x=120, y=150)
telephoneEntr.place(x=120, y=200)
matriculEntr.place(x=120, y=250)
classeEntr.place(x=120, y=300)


bout1= Button(pagePage, text="ENVOYER", bd=3, relief=RIDGE, width=10, height=2, command=valid )
bout2= Button(pagePage, text="REINITIALISER", bd=3, relief=RIDGE, width=10, height=2, command=reint )

bout1.place(x=10, y=400 )
bout2.place(x=110, y=400 )


def pag():
    for x in range(1):
        pagePage.place(x=x, y=y)
        #topFrame.update()

def pagferm():
    for x in range(650):
        pagePage.place(x=-x, y=y)
        #topFrame.update()

fermePag = tkinter.Button(pagePage, image=close, bg=couleur["white"],
                          activebackground=couleur["purple"], bd=0, command= pagferm )
fermePag.place(x=570, y=10)

#==================parametrage du BOUTON PROFIL===============

pageProfil= tkinter.Frame(app, bg="blue",width=600 ,height=600 , bd=0 )

ecole1 =Button(pageProfil, text="Abidjan ", font='Time 20 bold', relief=RIDGE, bd=5, width=13 )
ecole2 =Button(pageProfil, text="Bouaké ", font='Time 20 bold', relief=RIDGE, bd=5, width=13 )
ecole3 =Button(pageProfil, text="Korogho ", font='Time 20 bold', relief=RIDGE, bd=5, width=13 )
ecole4 =Button(pageProfil, text="Yamoussoukro ", font='Time 20 bold', relief=RIDGE, bd=5, width=13 )
ecole5 =Button(pageProfil, text="Man ", font='Time 20 bold', relief=RIDGE, bd=5, width=13 )

ecole1.place(x=10, y=50)
ecole2.place(x=10, y=120)
ecole3.place(x=10, y=190)
ecole4.place(x=10, y=260)
ecole5.place(x=10, y=330)


def profil():
    for x in range(3):
        pageProfil.place(x=x, y=y)
        topFrame.update()

def profilferm():
    for x in range(650):
        pageProfil.place(x=-x, y=y)
        #topFrame.update()

fermeProfil = tkinter.Button(pageProfil, image=close, bg=couleur["white"],
                          activebackground=couleur["purple"], bd=0, command= profilferm )
fermeProfil.place(x=550, y=10)


#==================parametrage du BOUTON PARAMETRE=======================

pageParametr= tkinter.Frame(app, bg='yellow', width=600, height=600 )

topFram1=tkinter.Frame(app, bg='blue', width=600, height=600 )
def para1():
    for x in range(-300, 0):
        topFram1.place(x=x, y=100)
        topFrame.update()
def paraferm1():
    for x in range(600):
        topFram1.place(x=-x, y=0)
        #topFrame.update()

compt1= Button(pageParametr, text="parametre1", font='Time 20 bold', relief=RIDGE, bd=5, width=13, command=para1 )
compt2= Button(pageParametr, text="parametre2", font='Time 20 bold', relief=RIDGE, bd=5, width=13)
compt3= Button(pageParametr, text="parametre3", font='Time 20 bold', relief=RIDGE, bd=5, width=13)
compt4= Button(pageParametr, text="parametre4", font='Time 20 bold', relief=RIDGE, bd=5, width=13)
compt5= Button(pageParametr, text="Déconnecter", font='Time 20 bold', relief=RIDGE, bd=5, width=13)
compt6= Button(pageParametr, text="Quitter ", font='Time 20 bold', relief=RIDGE, bd=5, width=13, command=quit )

compt1.place(x=10 , y=50)
compt2.place(x=10 , y=120)
compt3.place(x=10 , y=190)
compt4.place(x=10 , y=260)
compt5.place(x=10 , y=330)
compt6.place(x=10 , y=400)

def parametre():
    for x in range(3):
        pageParametr.place(x=x, y=y)
        topFrame.update()

def paraferm():
    for x in  range(650):
        pageParametr.place(x=-x, y=y)

fermeparamet = tkinter.Button(pageParametr, image=close, bg=couleur["white"],
                          activebackground=couleur["purple"], bd=0, command= paraferm )
fermeparamet.place(x=570, y=10)

fermeparamet1 = tkinter.Button(topFram1, image=close, bg=couleur["white"],
                          activebackground=couleur["purple"], bd=0, command= paraferm1 )
fermeparamet1.place(x=570, y=10)

#================parametrage du BOUTON AIDE ====================

page_aide= tkinter.Frame(app, bg='blue', width=600, height=600)

nom= Label(page_aide, text='AIDE ',  font='Time 20 bold', relief=RIDGE, bd=5, width=13 )
nom.place(x=10, y=50)

btnEtatopt= False
def aide():
        for x in range(-300, 0):
            page_aide.place(x=x, y=y)
            topFrame.update()

def aideferm():
        for x in range(650):
            page_aide.place(x=-x, y=y)
            #topFrame.update()


fermeaid = tkinter.Button(page_aide, image=close, bg=couleur["white"],
                          activebackground=couleur["purple"], bd=0, command=aideferm )
fermeaid.place(x=550, y=10)


#======================positionnement des options sur la page========================

    #===================1er methode===========================
tkinter.Button(page, text=option[0], font="ExtraCondensed 15",
               bg="gray30", fg=couleur["white"], activebackground='gray30', bd=0, command=acc ).place(x=40, y=60 )
tkinter.Button(page, text=option[1], font="ExtraCondensed 15",
               bg="gray30", fg=couleur["white"], activebackground='gray30', bd=0, command=pag ).place(x=40, y=100 )
tkinter.Button(page, text=option[2], font="ExtraCondensed 15",
               bg="gray30", fg=couleur["white"], activebackground='gray30', bd=0, command=profil ).place(x=40, y=140 )
tkinter.Button(page, text=option[3], font="ExtraCondensed 15",
               bg="gray30", fg=couleur["white"], activebackground='gray30', bd=0, command=parametre ).place(x=40, y=180 )
tkinter.Button(page, text=option[4], font="ExtraCondensed 15",
               bg="gray30", fg=couleur["white"], activebackground='gray30', bd=0, command=aide ).place(x=40, y=220 )

        #=====================2er methode=============================
#for i in range(5):
#    tkinter.Button(page, text=option[i], font="ExtraCondensed 15",
#               bg="gray30", fg=couleur["white"], activebackground='gray30', bd=0 , command=choix ).place(x=25, y=y )
#    y+= 40

#====================#==========================#=================

app.mainloop()