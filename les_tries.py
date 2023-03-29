
#--------------------- sort / sorted (trier)-------------

"""noms= ["bah", "alexandre", "alice", "jean", "maire", "nogues"]
#noms.sort() #inplace
#nom= sorted(noms, reverse=True)

noms.sort(key=lambda nom: len(nom))
print(noms)"""

#--------------trie avec fonction----------------------------

"""def trie_fonction(nom):
    return len(nom)

noms= ["bah", "alexandre", "alice", "jean", "maire", "nogues"]

noms.sort( key=trie_fonction )
nom_trie =sorted(noms, key=trie_fonction , reverse=True)


print(noms)
print(nom_trie)"""

#--------elements min, max, in, sum---------

"""noms= ["bah", "alexandre", "alice", "jean", "maire", "nogues"]

age =[21, 34, 54, 32, 28, 19]
#print(min(age))


if "alice" in noms:
    print('present')
else:
    print("absente")"""

#--------------------------------------

"""noms= ["bah", "alexandre", "alice", "jean", "maire", "nogues"]

age =[21, 34, 54, 32, 28, 19]
#print(min(age)) 

found = False
for nom in noms:
    if nom=='jean':
        found = True
        break
if found:
    print('present')
else:
    print('absent')

print(sum(age))"""
#
#------------------------------<>---------------------------
#
#---------------echanger les positions des elements de la liste-------------

"""noms= ["bah", "alexandre", "alice", "jean", "maire", "nogues"]

age =[21, 34, 54, 32, 28, 19]

#t =noms[0]
 #noms[0]= noms[4]
#noms[4]=t

noms[0], noms[4] = noms[0], noms[4]
print(noms)

noms[0], noms[4] = noms[4], noms[0]
print(noms)
"""
#------------------------------------join / split-------------------------------------

"""noms= ["bah", "alexandre", "alice", "jean", "maire", "nogues"]
#print(noms)
nm_join= ", ".join(noms)
print(nm_join)
print()

nom = "paul, toto, yao, jonas"
nm_split = nom.split()
print(nm_split)
"""

#-----------------index/ find/ count-------------------

#-----------------index-----------------
"""noms= ["bah", "alexandre", "alice", "jean", "maire", "nogues"]
#print(noms.index("jeane"))

element_chercher= "nogues"
if element_chercher in noms:
    print("l'element chercher est ",element_chercher)
    print(" il est à la ",noms.index(element_chercher)," position")
else:
    print("l'element chercher n'est pas dans ce tableau")
"""

#----------------------count---------
#noms= ["bah", "alexandre", "alice", "jean", "marie", "nogues"]
"""noms= "bah alexandre alice jean marie nogues"
nm_split= noms.split()
#print(nm_split)

element_chercher= "alice"
nb_occurence = nm_split.count(element_chercher)
print()
print("nombre d'occurence " ,nb_occurence)
print()

if nb_occurence > 0:
  index_occurence = 0
  for i in range(nb_occurence):
      index_occurence = nm_split.index(element_chercher , index_occurence)
      print(element_chercher, " est à la ", index_occurence, " position de la liste")
      index_occurence +=1
else:
    print("l'element chercher n'est pas dans ce tableau")"""

#--------find--------

"""a = "paul-eric, toto, ahy"
i = a.find("eric")
print(i)"""


personne= ["bah", "toto", "agathe", "olivia"]




