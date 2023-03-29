#
#
#
#
#------------------<>-----------------

def table_multiplication():
    nb_min= 15
    nb_max= 11
    if nb_min > nb_max:
        print("erreur, le nombre minimale est suerieur")

    for i in range(nb_min, nb_max):
        nb= 4
        print(i, "x", int(nb), "=",i*nb)

    print("-------------Fin du programme------------")
table_multiplication()