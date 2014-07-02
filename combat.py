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
            else:
            #il s'agit d'un sort



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
    def appliqueSort(arraySort):
        #on attend un array de type [id sort, type cible, id cible]

#fonction de combat
#je m'en occupe

#fonction qui recoit un objet sort avec une cible et qui verifie si la cible du sort est bien dans les cible possible de l'objet sort


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
        else
            blocSort.append(objCible.id)

        arrayTempSortTour.append(blocSort)
        objJoueur.pointMana['blanc'] -= objSort.coutInvocation['blanc']
        objJoueur.pointMana['rouge'] -= objSort.coutInvocation['rouge']
        objJoueur.pointMana['noir'] -= objSort.coutInvocation['noir']
        objJoueur.pointMana['bleu'] -= objSort.coutInvocation['bleu']
        objJoueur.pointMana['vert'] -= objSort.coutInvocation['vert']

        if objSort.coutInvocation['incolore'] > 0:
            decrementeIncolore(objJoueur, objSort.coutInvocation['incolore'])

#fonction qui decompte dun joueur le nombre dincolore passer en parametre et modifie la couleur dinvocation de le creature
    def decrementeIncolore(objJoueur, nbIncolor):
        """ --- a faire --- """
        print('a faire')
    
    
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






