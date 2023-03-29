#
#
#
def element_liste(e, liste ):
    """for el in liste :
        if e.lower() == el.lower():
            return True
        return False"""

    return e.lower() in liste


nom= ['bah', 'alex', 'alice', 'jean', "maire", "nogues"]

if element_liste("bAh", nom):
    print(" bah est là")
else:
    print("il n'existe pas dans la liste")


