class combat: #declaration class
    
    def __init__(self):#constructeur
        self.arrayAction = []
        self.arrayCreatureAttack = []
        sefl.arrayCreature = []
        self.arrayTempSortTour = []

#fonction qui ajoute un array dans la liste
    def addArrayInList(aSortCombat):
        arrayAction.append(aSortCombat)

#fonction qui ajoute en debut de liste
    def addArrayCreatureInList(aCreatureCombat):
        #comme cela on est sur que les creature soient en premier
        arrayAction.insert(0, aCreatureCombat)


#fonction qui parcour la liste et trie les sort des attaque
    def trieList():
        arrayAction.reverse()
        for monTableau in arrayAction:
            if(len(monTableau) < 3):
            #il s'agit des creatures
            else:
            #il s'agit d'un sort



#fonction qui prend les attaque et la place en fin de la liste
    def checkPositionCreature():
        if(len(arrayAction) != 2):
        
            indice = 0
            i = 0 # Notre indice pour la boucle while
            while i < len(ma_liste):
                if(len(arrayAction)==2):
                    indice = i
                
                i += 1 # On incrémente i, ne pas oublier !

            addArrayCreatureInList(arrayAction[indice])
            del arrayAction[indice+1]


#fonction applique les sort
    def appliqueSort(arraySort):
        #on attend un array de type [id sort, type cible, id cible]

#fonction de combat
#je m'en occupe

#fonction qui recoit un objet sort avec une cible et qui verifie si la cible du sort est bien dans les cible possible de l'objet sort


#fonction qui vérifie si une creature est vivante ou non

#fonction qui transfer le contenu de arrayTempSortTour dans arrayAction

#fonction qui supprime une action sort dans le tableau temporaire arrayTempSortTour et recrédite le mana de la carte dans la quantité de mana du joueur

#fonction qui ajoute un array sort dans arrayTempSortTour et qui déduit le cout de mana de la carte de la quantité du joueur
