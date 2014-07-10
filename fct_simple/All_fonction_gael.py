from creature_carac_modif import*
from fct_pioche import*
from joueur import*
from sort import*
from terrain import*
from creature import*
from carte import*
import random

#60 ingeniosite de jace pioche 3 carte
"""fait"""
def ingeniosite_de_jace(objJoueur):
	pioche(objJoueur,3,X,Y) """ attention il faut saisir des coordonnee generique de cimetiere ici """


#print(ingeniosite_de_jace([1,2,3,4,5,6],[7,8,9,10,11,12]))

"""fait"""
#25_raise_the_alarm ajoute 1/1 a une creature
def raise_the_alarm(creature):
	creature_carac_modif(creature,1,1)

	
#52_ecurage_de_pensee envoi 2 premieres cartes du deck dans le cimetiere
"""fait"""
def ecurage_de_pensee(objJoueur deck,cimetiere):
	i=0
	for i in range(2):#parcourt a 3 reprises le deck
		objJoueur.cimetiere.append(objJoueur.bibliotheque[0])#rajoute premiere carte du deck dans le cimetiere
		del objJoueur.bibliotheque[0] #supprime la carte du deck

	
#~ all = ecurage_de_pensee([1,2,3,4,5,6],[])
#~ print(all['deck'])
#~ print(all['cimetiere'])


#fonction pour check si le joueur est en vie
"""fait"""
def check_player_alive(objJoueur):
	if objJoueur.pointDeVie == 0 or len(objJoueur.bibliotheque) == 0:
		return TRUE
    else :
		return FALSE
		


#check la main du joueur
"""fait"""
def check_player_hand(joueur):
	if len(joueur.main)>7:
		return TRUE
	else:
		return FALSE


#fct modification caract creature
"""fait"""
def creature_carac_modif(creature,vie,degat):
    creature.vie += vie#modifie la vie de la creature
    creature.degat += degat#modifie les degat de la creature

    

#fction de recherche de carte et deplacement
""" je ne comprend pas ce que dois faire cette fonction"""
def search_and_move(objJoueur,card,position):
    card_ID=card.idCarte  
    cpt=len(objJoueur.bibliotheque)
    i=0
    
    while objJoueur.bibliotheque[i].idCarte!=card_ID :#recherche de la carte dans le deck
        i=i+1

    objJoueur.bibliotheque.insert(position-1,deck[i])
    del objJoueur.bibliotheque[i]""" est tu sur avec le insert la carte peut avoir bouger de son i"""


#melange orgainse du deck pour le debut de partie

#melange orgainse du deck pour le debut de partie

def deck_mix_first(deck):
	
    deck_inter_monstre_sort=[]#deck intermediaire pour stocker les cartes monstre et sort
    deck_inter_terrain=[]#deck intermediaire pour stocker les cartes terrain
    deck_melanger=[]
    r=0
    i=0
    cpt=len(deck)#compteur de cartes dans le deck
    
    for i in range(cpt):

        if (type(deck[i]) is creature) or (type(deck[i])is sort) :#carte type monstre et sort (provisoir en attente de la methode d'identification des 
            deck_inter_monstre_sort.append(deck[i])#deplacement de la carte
        elif type(deck[i]) is terrain :#carte de type terrain
            deck_inter_terrain.append(deck[i])
            
    cpt_t=len(deck_inter_terrain)#compteur carte terrain
    cpt_m_s=len(deck_inter_monstre_sort)#compteur carte monstre et sort
    #rep_ct_t=cpt_m_s//cpt_t#calcule de l'alternance avec les carte terrrain
    i=0
    
    #while (len(deck_inter_terrain)>0)and(len(deck_inter_monstre_sort)>0):
    for val in deck:    
        for i in range(2): #deplacement des carte monstre et terrain dans le deck
           if(len(deck_inter_monstre_sort) !=0):
              r=random.randint(0,len(deck_inter_monstre_sort)-1)
              deck_melanger.append(deck_inter_monstre_sort[r])
              del (deck_inter_monstre_sort[r])

        #deplacement des cartes terrain dans le deck
        if(len(deck_inter_terrain))!=0:
           r=random.randint(0,len(deck_inter_terrain)-1)
           deck_melanger.append(deck_inter_terrain[r])

    return deck_melanger



"""fait"""
#pioche des cartes dans le deck
def pioche(objJoueur,nb_carte,X,Y):
    i=0
    for i in range(nb_carte):
        objJoueur.bibliotheque[i].x = X
        objJoueur.bibliotheque[i].y = Y
        objJoueur.main.append(objJoueur.bibliotheque[i]) #ajout des cartes du deck dans la main du joueur
        del objJoueur.bibliotheque[i]

#print(pioche(deck=[1,2,3,4,5,6,7,8,9,10],main_joueur=[11,12,13,14,15,16],nb_carte=10))


#melange du deck 
"""fait"""
def deck_mix(objJoueur):
	deck_melanger=[]#definition deck melanger 
	r=0
	i=0
	cpt=len(objJoueur.bibliotheque)
	#transfert de carte aleatoirement dans le deck melanger
	for  i in range(cpt):
		r=random.randint(0,len(objJoueur.bibliotheque)-1)#nb aleatoire entre 0 et la derniere case du deck de depart
		deck_melanger.append(objJoueur.bibliotheque[r])#deplacement de la carte dans le deck intermediaire
		del objJoueur.bibliotheque[r]#supression de la carte transferee

    objJoueur.bibliotheque = deck_melanger

#print(deck_mix(deck=[1,2,3,4,5,6]))#test fonctionnement fct deck_mix


#envoie carte de la main vers les cartes posee
"""fait"""
def hand_to_game(objJoueur,card,X,Y):
	i=0
	while objJoueur.main[i].idCarte != card.idCarte:
		i=i+1
		
    objJoueur.main[i].x = X
    objJoueur.main[i].y = Y
	objJoueur.cartePose.append(objJoueur.main[i])
	del objJoueur.cartePose[i]

#envoie carte d'un repertoire vers le cimetiere
"""fait"""
def cimetiere(objJoueur,card,X,Y):
	i=0
	if card in objJoueur.cartePose:
        while objJoueur.cartePose[i].idCarte != card.idCarte:
            i=i+1
		
        objJoueur.cartePose[i].x = X
        objJoueur.cartePose[i].y = Y
        objJoueur.cimetiere.append(objJoueur.cartePose[i])
        del objJoueur.cartePose[i]
            
    elif card in objJoueur.main:
        while objJoueur.main[i].idCarte != card.idCarte:
            i=i+1
		
        objJoueur.main[i].x = X
        objJoueur.main[i].y = Y
        objJoueur.cimetiere.append(objJoueur.main[i])
        del objJoueur.main[i]

    elif card in objJoueur.bibliotheque:
        while objJoueur.bibliotheque[i].idCarte != card.idCarte:
            i=i+1
		
        objJoueur.bibliotheque[i].x = X
        objJoueur.bibliotheque[i].y = Y
        objJoueur.cimetiere.append(objJoueur.bibliotheque[i])
        del objJoueur.bibliotheque[i]


#envoie carte du cimetiere vers la main
"""fait"""
def cimetiereToHand(objJoueur,card , X ,Y):
	i=0
	while objJoueur.cimetiere[i].idCarte != card.idCarte:
		i=i+1
		
    objJoueur.cimetiere[i].x = X
    objJoueur.cimetiere[i].y = Y
	objJoueur.main.append(objJoueur.cimetiere[i])
	del objJoueur.cimetiere[i]

#envoie carte du cimetiere vers le plateau
"""fait"""
def cimetiereToField(objJoueur,card, X ,Y):
	i=0
	while objJoueur.cimetiere[i].idCarte != card.idCarte:
		i=i+1
    
    objJoueur.cimetiere[i].x = X
    objJoueur.cimetiere[i].y = Y
	objJoueur.cartePose.append(objJoueur.cimetiere[i])
	del objJoueur.cimetiere[i]

#retour un objet carte en fonction des coordonnee x et y
def recupObjCarteWithCoord(objJoueur,X,Y):
    myCarte = null
    for elt in objJoueur.main:
        if elt.x == X and elt.y == Y
            myCarte = elt

    for elt in objJoueur.cartePose:
        if elt.x == X and elt.y == Y
            myCarte = elt

    return myCarte

#test si le joueur a suffisement de mana pour joueur la carte
def checkManaForPlay(objJoueur, objCarte):
    pouvoir = TRUE
    if objCarte.coutInvocation['blanc'] > 0:
        if  objJoueur.pointMana['blanc'] < objCarte.coutInvocation['blanc']
            pouvoir = FALSE
    elif objCarte.coutInvocation['rouge'] > 0:
        if  objJoueur.pointMana['rouge'] < objCarte.coutInvocation['rouge']
            pouvoir = FALSE
    elif objCarte.coutInvocation['noir'] > 0:
        if  objJoueur.pointMana['noir'] < objCarte.coutInvocation['noir']
            pouvoir = FALSE
    elif objCarte.coutInvocation['bleu'] > 0:
        if  objJoueur.pointMana['bleu'] < objCarte.coutInvocation['bleu']
            pouvoir = FALSE
    elif objCarte.coutInvocation['vert'] > 0:
        if  objJoueur.pointMana['vert'] < objCarte.coutInvocation['vert']
            pouvoir = FALSE
    elif objCarte.coutInvocation['incolore'] > 0:
        somme = objJoueur.pointMana['blanc'] + objJoueur.pointMana['rouge'] + objJoueur.pointMana['noir'] + objJoueur.pointMana['bleu'] + objJoueur.pointMana['vert']

        if somme < objCarte.coutInvocation['incolore']:
             pouvoir = FALSE
    return pouvoir

#fonction qui test si un terrain a ete pose ou non pendant ce tour
# recoit un objet joueur
def checkLandField(objJoueur):
    if objJoueur.terrainPoserTour == 0:
        return false
    else:
        return true

#fonction qui test si une carte est engage ou non
# recoit un objet carte
def checkCardEngaged(listeJoueur,objCard):
    engaged = false
    for joueur in listeJoueur:
        if objCard in joueur.carteEngage:
            engaged = true
    return engaged

#fonction qui verifie si un objet creature peut jouer ou pas "mal d'invocation"
#prendre en compte la celerite des creatures
def checkinvocatiuon(objCreature):
    if objCreature.mal_invocation == 0 or "celerite" in objCreature.caracteristique:
        return true
    else:
        return false

#fonction qui parcour en debut de tour les creature du joueur sur le plateau et enleve le mal d invocation a ceux qui lon
def setInvocation():
    for joueur in listeJoueur:
        for creature in joueur.cartePose:
            if creature.mal_invocation == 1:
                creature.mal_invocation = 0

def engagedMana(objJoueur, objCarte):
    objJoueur.pointMana['blanc'] += objCarte.mana['blanc']
    objJoueur.pointMana['rouge'] += objCarte.mana['rouge']
    objJoueur.pointMana['noir'] += objCarte.mana['noir']
    objJoueur.pointMana['bleu'] += objCarte.mana['bleu']
    objJoueur.pointMana['vert'] += objCarte.mana['vert']

    objCarte.url_img = 'a'+objCarte.url_img
    objJoueur.carteEngage.append(objCarte)



def desengagedMana(objJoueur, objCarte):
    objJoueur.pointMana['blanc'] -= objCarte.mana['blanc']
    objJoueur.pointMana['rouge'] -= objCarte.mana['rouge']
    objJoueur.pointMana['noir'] -= objCarte.mana['noir']
    objJoueur.pointMana['bleu'] -= objCarte.mana['bleu']
    objJoueur.pointMana['vert'] -= objCarte.mana['vert']
    
    i = 0
    while objJoueur.carteEngage[i].idCarte != objCarte.idCarte:
		i=i+1
    objCarte.url_img = objCarte.url_img[1:len(objCarte.url_img)]
    del objJoueur.bibliotheque[i]






