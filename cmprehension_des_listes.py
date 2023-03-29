#------------------------------<>---------------------------
#------------------------------<>---------------------------
#------------------------------<>---------------------------

noms= ["bah", "alexandre", "alice", "jean", "marie", "nogues"]

"""long = []
for nom in noms:
    long .append(len(nom))
print(long)
"""
long = [len(nom) for nom in noms if len(nom) < 5 ]

long_caract = [nom for nom in noms if "i" in nom ]

long_inf = [len(nom) if len(nom) < 5  else 0 for nom in noms  ]

print(long)
print(long_caract)
print(long_inf)

#a= [i for i in range(8) if (i/2) ]
a = [True if (i//2)*2 == i  else False for i in range(5)  ]

print(a)


