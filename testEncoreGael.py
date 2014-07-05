from carte import *

i=0	
for i in range(3):
    print(i)



ma_liste = [-5, -2, 1, 4, 7, 10]
print(ma_liste)
print(ma_liste[0])
print("--------")
del(ma_liste[0])
print(ma_liste)
print(ma_liste[0])
print("--------")
"""
def changeColor(objCarte):
    objCarte.couleurCarte = "bleu"

def invocationChange(listeCouleur):
    listeCouleur['noir'] += 2
    return listeCouleur

listeCarte = []
main = []

maCarte1 = carte("ecureuil", 12, "toto", "rouge")
maCarte2 = carte("banane", 22, "...toto...", "rouge")
maCarte3 = carte("flan", 2, "miam", "rouge")
maCarte4 = carte("poire", 32, "nouille", "rouge")

listeCarte.append(maCarte1)
listeCarte.append(maCarte2)
listeCarte.append(maCarte3)
listeCarte.append(maCarte4)

for elt in listeCarte:
    print(elt.coutInvocation)
print("-----------------")

main.append(listeCarte[1])
main.append(listeCarte[3])

for elt in main:
    print(elt.coutInvocation)

print("--------- Masse --------")

listeCarte[3].coutInvocation = invocationChange(listeCarte[3].coutInvocation)

for elt in listeCarte:
    print(elt.coutInvocation)

print("-----------------")

for elt in main:
    print(elt.coutInvocation)
    
"""
"""
print("-----first liste -----")

for elt in listeCarte:
    print(elt.couleurCarte)

changeColor(maCarte2)
print("----------------------")

for elt in listeCarte:
    print(elt.couleurCarte)


changeColor(listeCarte[2])
print("-----------------------")
for elt in listeCarte:
    print(elt.couleurCarte)


print("----- second liste -----")

for elt in main:
    print(elt.couleurCarte)

changeColor(maCarte4)
print("-----------------------")

for elt in main:
    print(elt.couleurCarte)
print("-----------------------")

listeCarte[1].couleurCarte = "rouge"

for elt in main:
    print(elt.couleurCarte)
"""
