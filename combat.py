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
            if len(monTableau) < 3 :
            #il s'agit des creatures
                combatCreature(monTableau)
            else:
            #il s'agit d'un sort
                appliqueSort(monTableau)



#fonction qui prend les attaque et la place en fin de la liste
    def checkPositionCreature():
        if len(arrayAction) != 2 :
        
            indice = 0
            i = 0 # Notre indice pour la boucle while
            while i < len(ma_liste):
                if len(arrayAction)==2 :
                    indice = i
                
                i += 1 # On incrémente i, ne pas oublier !

            addArrayCreatureInList(arrayAction[indice])
            del arrayAction[indice+1]


#fonction applique les sort
    def appliqueSort(arraySort): """pas encore faite """
        #on attend un array de type [id sort, type cible, id cible]
        """voila je pense que un dictionnaire de fonction ferai laffaire avec toujours les memes parametre et ce serai chaque fonction qui genre ne interne les parametres"""



#fonction de combat
#je m'en occupe
    def combatCreature(blocCreature):

#fonction qui recoit un objet sort avec une cible et qui verifie si la cible du sort est bien dans les cible possible de l'objet sort
    def testCible(cible, objSort):""" je ne sais pas si on dois recevoir le conteneur ou la cible uniquement """
        if objSort.cibleSort[cible] = 1:
            return true
        else:
            return false

#fonction qui vérifie si une creature est vivante ou non
    def verifCreatLife(maCreat):
        if maCreat.vie > 0:
            return true
        else:
            return false

#fonction qui transfer le contenu de arrayTempSortTour dans arrayAction
    def transferArrayTempToArrayAction():
        for blocSort in arrayTempSortTour:
            arrayAction.append(blocSort)


#fonction qui supprime une action sort dans le tableau temporaire arrayTempSortTour et recrédite le mana de la carte dans la quantité de mana du joueur
    def cancelSort(objJoueur, objSort):

        i = 0 # Notre indice pour la boucle while
        while i < len(arrayTempSortTour):
            if objSort.idCarte == arrayTempSortTour[i][0]:
                objJoueur.pointMana['blanc'] += objSort.coutInvocation['blanc']
                objJoueur.pointMana['rouge'] += objSort.coutInvocation['rouge']
                objJoueur.pointMana['noir'] += objSort.coutInvocation['noir']
                objJoueur.pointMana['bleu'] += objSort.coutInvocation['bleu']
                objJoueur.pointMana['vert'] += objSort.coutInvocation['vert']

                del arrayTempSortTour[i]
                i=len(arrayTempSortTour)
            else:
                i += 1 # On incrémente i, ne pas oublier !


#fonction qui ajoute un array sort dans arrayTempSortTour et qui déduit le cout de mana de la carte de la quantité du joueur
    def addSortToTemp(objJA,objSort,objCible,typeCible):
        blocSort = []
        blocSort.append(objSort.idCarte)
        blocSort.append(typeCible)
        if typeCible == "joueur":
            blocSort.append(objCible.idCarte)
        else:
            blocSort.append(objCible.id)

        arrayTempSortTour.append(blocSort)
        objJoueur.pointMana['blanc'] -= objSort.coutInvocation['blanc']
        objJoueur.pointMana['rouge'] -= objSort.coutInvocation['rouge']
        objJoueur.pointMana['noir'] -= objSort.coutInvocation['noir']
        objJoueur.pointMana['bleu'] -= objSort.coutInvocation['bleu']
        objJoueur.pointMana['vert'] -= objSort.coutInvocation['vert']

        if objSort.coutInvocation['incolore'] > 0:
            decrementeIncolore(objJoueur, objSort)

#fonction qui decompte dun joueur le nombre dincolore passer en parametre et modifie la couleur dinvocation de le creature
    def decrementeIncolore(objJoueur, objCarte):
        
        while objSort.coutInvocation['incolore'] != 0:
            if objJoueur.pointMana['blanc'] > 0:
                objJoueur.pointMana['blanc'] -= 1
                objSort.coutInvocation['blanc'] += 1
                objSort.coutInvocation['incolore'] -= 1
            elif objJoueur.pointMana['rouge'] > 0:
                objJoueur.pointMana['rouge'] -= 1
                objSort.coutInvocation['rouge'] += 1
                objSort.coutInvocation['incolore'] -= 1
            elif objJoueur.pointMana['noir'] > 0:
                objJoueur.pointMana['noir'] -= 1
                objSort.coutInvocation['noir'] += 1
                objSort.coutInvocation['incolore'] -= 1
            elif objJoueur.pointMana['bleu'] > 0:
                objJoueur.pointMana['bleu'] -= 1
                objSort.coutInvocation['bleu'] += 1
                objSort.coutInvocation['incolore'] -= 1
            elif objJoueur.pointMana['vert'] > 0:
                objJoueur.pointMana['vert'] -= 1
                objSort.coutInvocation['vert'] += 1
                objSort.coutInvocation['incolore'] -= 1

    
    
#fonction qui recoit la creature attaquant et la creature bloqueuse et qui verifie si on peut bloquer ou non
    def testBloquageCreature(creatAttaq, creatBloqu):
        #on met a default bloquer a false et on test uniquement les cas ou une creature peut bloquer
        #c est plus facile et on est sur de ne pas se tromper
        bloquer = false
        
        #on fera en amont le test si la creature est engage ou non avant de arriver ici
        if len(creatAttaq.caracteristique) != 0:
            for caract in creatAttaq.caracteristique:
                if caract == "vol":
                    if "vol" in creatBloqu.caracteristique:
                        bloquer = true
                elif caract == "distortion":
                    if "distortion" in creatBloqu.caracteristique:
                        bloquer = true
                elif caract == "equitation":
                    if "equitation" in creatBloqu.caracteristique:
                        bloquer = true
                elif caract == "peur":
                    if creatBloqu.couleurCarte == "noir":
                        bloquer = true
                elif caract == "intimidation":
                    if creatAttaq.couleurCarte == creatBloqu.couleurCarte:
                        bloquer = true
        elif len(creatBloqu.caracteristique) != 0:
            for caract in creatBloqu.caracteristique:
                if caract != "distortion":
                    bloquer = true
        else:
            bloquer = true






