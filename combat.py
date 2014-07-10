class combat: #declaration class
    
    def __init__(self):#constructeur
        self.arrayAction = []
        self.arrayCreatureAttack = []
        self.arrayCreature = []
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

#fonction qui retourne un objet joueur qui possede la creature
    def joueurToCreature(objCreature):
        for joueur in listeJoueur:
            if objCreature in joueur.cartePose:
                return joueur

#fonction qui retourne un objet joueur qui ne possede pas la creature plus vicieux
def joueurNotToCreature(objCreature):
    for joueur in listeJoueur:
        if objCreature not in joueur.cartePose:
            return joueur


#fonction de combat
    def combatCreature(blocCreature):
        #blocCreature[0] -> attaquant
        #blocCreature[1] -> bloqueur
        
        #ici on test si il y a un bloqueur pour la creature qui attaque
        #if Object is None:
            
        if type(blocCreature[1]) is creature:
            theAttaq = joueurToCreature(blocCreature[0])
            thedef = joueurToCreature(blocCreature[1])
            
            if len(blocCreature[0].caracteristique) > 0:
                for caract in blocCreature[0].caracteristique:
                    if caract == "contact mortel":
                        if len(blocCreature[1].caracteristique)>0:
                            if "indestructible" in blocCreature[1].caracteristique:
                                blocCreature[0].vie -= blocCreature[1].degat
                            if "contact mortel" in blocCreature[1].caracteristique:
                                blocCreature[1].vie -= blocCreature[0].degat
                                blocCreature[0].vie -= blocCreature[1].degat
                                blocCreature[1].vie = 0
                                blocCreature[0].vie = 0
                            if "initiative" in blocCreature[1].caracteristique:
                                blocCreature[0].vie -= blocCreature[1].degat
                                if verifCreatLife(blocCreature[0]):
                                    blocCreature[1].vie -= blocCreature[0].degat
                                    blocCreature[1].vie = 0
                            if "double initiative" in blocCreature[1].caracteristique:
                                blocCreature[0].vie -= blocCreature[1].degat
                                if verifCreatLife(blocCreature[0]):
                                    blocCreature[1].vie -= blocCreature[0].degat
                                    blocCreature[0].vie -= blocCreature[1].degat
                                    blocCreature[1].vie = 0
                            if "lien de vie" in blocCreature[1].caracteristique:
                                theDef.pointDeVie += blocCreature[1].degat
                                blocCreature[1].vie -= blocCreature[0].degat
                                blocCreature[0].vie -= blocCreature[1].degat
                                blocCreature[1].vie = 0
                        else:
                            blocCreature[1].vie -= blocCreature[0].degat
                            blocCreature[0].vie -= blocCreature[1].degat
                            blocCreature[1].vie = 0
        
                    elif caract == "initiative":
                        if len(blocCreature[1].caracteristique)>0:
                            if "indestructible" in blocCreature[1].caracteristique:
                                blocCreature[0].vie -= blocCreature[1].degat
                            if "contact mortel" in blocCreature[1].caracteristique:
                                blocCreature[1].vie -= blocCreature[0].degat
                                if verifCreatLife(blocCreature[1]):
                                    blocCreature[0].degat = 0
                            if "initiative" in blocCreature[1].caracteristique:
                                blocCreature[1].vie -= blocCreature[0].degat
                                blocCreature[0].vie -= blocCreature[1].degat
                            if "double initiative" in blocCreature[1].caracteristique:
                                blocCreature[0].vie -= blocCreature[1].degat
                                blocCreature[1].vie -= blocCreature[0].degat
                                if verifCreatLife(blocCreature[1]):
                                    blocCreature[0].vie -= blocCreature[1].degat
                            if "lien de vie" in blocCreature[1].caracteristique:
                                blocCreature[1].vie -= blocCreature[0].degat
                                if verifCreatLife(blocCreature[1]):
                                    blocCreature[0].vie -= blocCreature[1].degat
                                    theDef.pointDeVie += blocCreature[1].degat
                        else:
                            blocCreature[1].vie -= blocCreature[0].degat
                            if verifCreatLife(blocCreature[1]):
                                blocCreature[0].vie -= blocCreature[1].degat
        
                    elif caract == "double initiative":
                        if len(blocCreature[1].caracteristique)>0:
                            if "indestructible" in blocCreature[1].caracteristique:
                                blocCreature[0].vie -= blocCreature[1].degat
                            if "contact mortel" in blocCreature[1].caracteristique:
                                blocCreature[1].vie -= blocCreature[0].degat
                                if verifCreatLife(blocCreature[1]):
                                    blocCreature[1].vie -= blocCreature[0].degat
                                    blocCreature[0].vie -= blocCreature[1].degat
                                    blocCreature[0].vie = 0
                            if "initiative" in blocCreature[1].caracteristique:
                                blocCreature[1].vie -= blocCreature[0].degat
                                blocCreature[0].vie -= blocCreature[1].degat
                                if verifCreatLife(blocCreature[0]):
                                    blocCreature[1].vie -= blocCreature[0].degat
                            if "double initiative" in blocCreature[1].caracteristique:
                                blocCreature[1].vie -= blocCreature[0].degat
                                blocCreature[0].vie -= blocCreature[1].degat
                                if verifCreatLife(blocCreature[0]) and  verifCreatLife(blocCreature[1]):
                                    blocCreature[1].vie -= blocCreature[0].degat
                                    blocCreature[0].vie -= blocCreature[1].degat
                            if "lien de vie" in blocCreature[1].caracteristique:
                                blocCreature[1].vie -= blocCreature[0].degat
                                if verifCreatLife(blocCreature[1]):
                                    blocCreature[1].vie -= blocCreature[0].degat
                                    blocCreature[0].vie -= blocCreature[1].degat
                                    theDef.pointDeVie += blocCreature[1].degat
                        else:
                            blocCreature[1].vie -= blocCreature[0].degat
                            if verifCreatLife(blocCreature[1]):
                                blocCreature[1].vie -= blocCreature[0].degat
                                blocCreature[0].vie -= blocCreature[1].degat
                    elif caract == "debordement":
                            blocCreature[1].vie -= 1
                            blocCreature[1].degat -= 1
                        if verifCreatLife(blocCreature[1]):
                            if len(blocCreature[1].caracteristique)>0:
                                if "indestructible" in blocCreature[1].caracteristique:
                                    blocCreature[0].vie -= blocCreature[1].degat
                                if "contact mortel" in blocCreature[1].caracteristique:
                                    blocCreature[1].vie -= blocCreature[0].degat
                                    blocCreature[0].vie -= blocCreature[1].degat
                                    blocCreature[0].vie = 0
                                if "initiative" in blocCreature[1].caracteristique:
                                    blocCreature[1].vie -= blocCreature[0].degat
                                        if verifCreatLife(blocCreature[1]):
                                            blocCreature[0].vie -= blocCreature[1].degat
                                if "double initiative" in blocCreature[1].caracteristique:
                                    blocCreature[1].vie -= blocCreature[0].degat
                                        if verifCreatLife(blocCreature[1]):
                                            blocCreature[0].vie -= blocCreature[1].degat
                                            blocCreature[1].vie -= blocCreature[0].degat
                                if "lien de vie" in blocCreature[1].caracteristique:
                                    theDef.pointDeVie += blocCreature[1].degat
                                    blocCreature[1].vie -= blocCreature[0].degat
                                    blocCreature[0].vie -= blocCreature[1].degat
                            else:
                                blocCreature[1].vie -= blocCreature[0].degat
                                blocCreature[0].vie -= blocCreature[1].degat
                    elif caract == "pietinement":
                        if len(blocCreature[1].caracteristique)>0:
                            if "indestructible" in blocCreature[1].caracteristique:
                                blocCreature[0].vie -= blocCreature[1].degat
                            if "contact mortel" in blocCreature[1].caracteristique:
                                if blocCreature[0].degat > blocCreature[1].vie:
                                    thedef.pointDeVie -= blocCreature[0].degat - blocCreature[1].vie
                                blocCreature[1].vie -= blocCreature[0].degat
                                blocCreature[0].vie -= blocCreature[1].degat
                                blocCreature[0].vie = 0
                            if "initiative" in blocCreature[1].caracteristique:
                                blocCreature[0].vie -= blocCreature[1].degat
                                if verifCreatLife(blocCreature[0]):
                                    if blocCreature[0].degat > blocCreature[1].vie:
                                        thedef.pointDeVie -= blocCreature[0].degat - blocCreature[1].vie
                                    blocCreature[1].vie -= blocCreature[0].degat
                            if "double initiative" in blocCreature[1].caracteristique:
                                blocCreature[0].vie -= blocCreature[1].degat
                                if verifCreatLife(blocCreature[0]):
                                    if blocCreature[0].degat > blocCreature[1].vie:
                                        thedef.pointDeVie -= blocCreature[0].degat - blocCreature[1].vie
                                    blocCreature[1].vie -= blocCreature[0].degat
                                    blocCreature[0].vie -= blocCreature[1].degat
                            if "lien de vie" in blocCreature[1].caracteristique:
                                if blocCreature[0].degat > blocCreature[1].vie:
                                    thedef.pointDeVie -= blocCreature[0].degat - blocCreature[1].vie
                                blocCreature[1].vie -= blocCreature[0].degat
                                blocCreature[0].vie -= blocCreature[1].degat
                                theDef.pointDeVie += blocCreature[1].degat
                        else:
                            if blocCreature[0].degat > blocCreature[1].vie:
                                thedef.pointDeVie -= blocCreature[0].degat - blocCreature[1].vie
                            blocCreature[1].vie -= blocCreature[0].degat
                            blocCreature[0].vie -= blocCreature[1].degat
                    elif caract == "indestructible":
                        blocCreature[1].vie -= blocCreature[0].degat
                        if len(blocCreature[1].caracteristique)>0:
                            if "lien de vie" in blocCreature[1].caracteristique:
                                theDef.pointDeVie += blocCreature[1].degat
                    elif caract == "lien de vie":
                        if len(blocCreature[1].caracteristique)>0:
                            if "indestructible" in blocCreature[1].caracteristique:
                                blocCreature[1].vie -= blocCreature[0].degat
                                blocCreature[0].vie -= blocCreature[1].degat
                                theAttaq.pointDeVie += blocCreature[0].degat
                            if "contact mortel" in blocCreature[1].caracteristique:
                                blocCreature[1].vie -= blocCreature[0].degat
                                blocCreature[0].vie -= blocCreature[1].degat
                                theAttaq.pointDeVie += blocCreature[0].degat
                                blocCreature[0].vie = 0
                            if "initiative" in blocCreature[1].caracteristique:
                                blocCreature[0].vie -= blocCreature[1].degat
                                if verifCreatLife(blocCreature[0]):
                                    blocCreature[1].vie -= blocCreature[0].degat
                                    theAttaq.pointDeVie += blocCreature[0].degat
                            if "double initiative" in blocCreature[1].caracteristique:
                                blocCreature[0].vie -= blocCreature[1].degat
                                if verifCreatLife(blocCreature[0]):
                                    blocCreature[1].vie -= blocCreature[0].degat
                                    blocCreature[0].vie -= blocCreature[1].degat
                                    theAttaq.pointDeVie += blocCreature[0].degat
                            if "lien de vie" in blocCreature[1].caracteristique:
                                blocCreature[1].vie -= blocCreature[0].degat
                                blocCreature[0].vie -= blocCreature[1].degat
                                theAttaq.pointDeVie += blocCreature[0].degat
                                theDef.pointDeVie += blocCreature[1].degat
                        else:
                            blocCreature[1].vie -= blocCreature[0].degat
                            blocCreature[0].vie -= blocCreature[1].degat
                            theAttaq.pointDeVie += blocCreature[0].degat
        #defenseur a des apt mais pas attaquant
            elif len(blocCreature[0].caracteristique) > 0:
                if "indestructible" in blocCreature[1].caracteristique:
                    blocCreature[0].vie -= blocCreature[1].degat
                if "contact mortel" in blocCreature[1].caracteristique:
                    blocCreature[1].vie -= blocCreature[0].degat
                    blocCreature[0].vie -= blocCreature[1].degat
                    blocCreature[0].vie = 0
                if "initiative" in blocCreature[1].caracteristique:
                    blocCreature[0].vie -= blocCreature[1].degat
                    if verifCreatLife(blocCreature[0]):
                        blocCreature[1].vie -= blocCreature[0].degat
                if "double initiative" in blocCreature[1].caracteristique:
                    blocCreature[0].vie -= blocCreature[1].degat
                    if verifCreatLife(blocCreature[0]):
                        blocCreature[1].vie -= blocCreature[0].degat
                        blocCreature[0].vie -= blocCreature[1].degat
                if "lien de vie" in blocCreature[1].caracteristique:
                    blocCreature[1].vie -= blocCreature[0].degat
                    blocCreature[0].vie -= blocCreature[1].degat
                    theDef.pointDeVie += blocCreature[1].degat
            else:
                #combat classique
                blocCreature[1].vie -= blocCreature[0].degat
                blocCreature[0].vie -= blocCreature[1].degat
        else:#si pas de creature bloqueuse le joueur prend tout
            thedef = joueurNotToCreature(blocCreature[0])
            thedef.pointDeVie -= blocCreature[0].degat


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
        blocSort.append(objSort)
        blocSort.append(typeCible)
        blocSort.append(objCible)
        """if typeCible == "joueur":
            blocSort.append(objCible)
        else:
            blocSort.append(objCible.id)"""

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


#fonction qui engage une creature attaquante
    def engageCreatureAttaque(objJoueur, objCreature):
        arrayCreatureAttack.append(objCreature)

        objJoueur.pointMana['blanc'] -= objCreature.coutInvocation['blanc']
        objJoueur.pointMana['rouge'] -= objCreature.coutInvocation['rouge']
        objJoueur.pointMana['noir'] -= objCreature.coutInvocation['noir']
        objJoueur.pointMana['bleu'] -= objCreature.coutInvocation['bleu']
        objJoueur.pointMana['vert'] -= objCreature.coutInvocation['vert']
        
        if objSort.coutInvocation['incolore'] > 0:
            decrementeIncolore(objJoueur, objCreature)

#fonction qui engage une creature de defence
    def engageCreatureAttaque(objJoueurDef, objCreatureAtt, objCreatureDef):

        blocCreat = []
        blocCreat.append(objCreatureAtt)
        blocCreat.append(objCreatureDef)
        
        addArrayCreatureInList(blocCreat)
    
        objJoueurDef.pointMana['blanc'] -= objCreatureDef.coutInvocation['blanc']
        objJoueurDef.pointMana['rouge'] -= objCreatureDef.coutInvocation['rouge']
        objJoueurDef.pointMana['noir'] -= objCreatureDef.coutInvocation['noir']
        objJoueurDef.pointMana['bleu'] -= objCreatureDef.coutInvocation['bleu']
        objJoueurDef.pointMana['vert'] -= objCreatureDef.coutInvocation['vert']
    
        if objSort.coutInvocation['incolore'] > 0:
            decrementeIncolore(objJoueurDef, objCreatureDef)

#fonction qui enleve une creature attaquante
    def desengageCreatureAttaque(objJoueur, objCreature):
        i = 0 # Notre indice pour la boucle while
        while i < len(arrayCreatureAttack):
            if objCreature.idCarte == arrayCreatureAttack[i].idCarte:
                objJoueur.pointMana['blanc'] += objCreature.coutInvocation['blanc']
                objJoueur.pointMana['rouge'] += objCreature.coutInvocation['rouge']
                objJoueur.pointMana['noir'] += objCreature.coutInvocation['noir']
                objJoueur.pointMana['bleu'] += objCreature.coutInvocation['bleu']
                objJoueur.pointMana['vert'] += objCreature.coutInvocation['vert']
                
                del arrayCreatureAttack[i]
                i=len(arrayCreatureAttack)
            else:
                i += 1 # On incrémente i, ne pas oublier !

#fonction qui enleve une creature de defense
    def desengageCreatureDefense(objJoueur, objCreature):
        i = 0 # Notre indice pour la boucle while
        while i < len(blocCreat):
            if objCreature.idCarte == blocCreat[i][1].idCarte:
                objJoueur.pointMana['blanc'] += objCreature.coutInvocation['blanc']
                objJoueur.pointMana['rouge'] += objCreature.coutInvocation['rouge']
                objJoueur.pointMana['noir'] += objCreature.coutInvocation['noir']
                objJoueur.pointMana['bleu'] += objCreature.coutInvocation['bleu']
                objJoueur.pointMana['vert'] += objCreature.coutInvocation['vert']
            
                del blocCreat[i]
                i=len(blocCreat)
            else:
                i += 1 # On incrémente i, ne pas oublier !







