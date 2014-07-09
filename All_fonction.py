#from creature_carac_modif import*
#from fct_pioche import*
from joueur import*
from sort import*
from terrain import*
from creature import*
from carte import*
import random

#60 ingeniosite de jace pioche 3 carte
def ingeniosite_de_jace(main_joueur,deck):
	
	main_joueur_final=[]
	
	main_joueur_final=pioche(deck,main_joueur,3)
	
	return main_joueur_final

#print(ingeniosite_de_jace([1,2,3,4,5,6],[7,8,9,10,11,12]))

#25_raise_the_alarm ajoute 1/1 a une creature
def raise_the_alarm(creature):
	
	creature=creature_carac_modif(creature,1,1)
	
	return creature
	
#52_ecurage_de_pensee envoi 2 premieres cartes du deck dans le cimetiere	
def ecurage_de_pensee(deck,cimetiere):
	
	i=0
	
	for i in range(3):#parcourt a 3 reprises le deck
		
		cimetiere.append(deck[0])#rajoute premiere carte du deck dans le cimetiere
		del(deck[0])#supprime la carte du deck
	deck_cimetiere={'deck':deck,'cimetiere':cimetiere}#tableau de hachage contenant le deck et le cimetiere
	return deck_cimetiere#retour du deck et du cimetiere
	
#~ all = ecurage_de_pensee([1,2,3,4,5,6],[])
#~ print(all['deck'])
#~ print(all['cimetiere'])


#fonction pour check si le joueur est en vie

def check_player_alive(joueur):
	
	if joueur.pointDeVie == 0:
		
		return TRUE
		
	elif joueur.bibliotheque == []:
	
		return TRUE
	
	else :
		
		return FALSE
		


#check la main du joueur

def check_player_hand(joueur):
	
	if len(joueur.main)>7:
		
		return TRUE
		
	else:
		
		return FALSE


#fct modification caract creature

def creature_carac_modif(creature,vie,degat):

    creature.vie=creature.vie+vie#modifie la vie de la creature
    creature.degat=creature.degat+degat#modifie les degat de la creature

    return creature
    

#fction de recherche de carte et deplacement

def search_and_move(deck,card,position):
    card_ID=card.idCarte  
    cpt=len(deck)
    i=0
    
    while deck[i].idCarte!=card_ID :#recherche de la carte dans le deck
        i=i+1

    deck.insert(position-1,deck[i])
    del(deck[i])

    return deck


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

#print(deck_mix_first(deck=[1,2,3,1,2,3,1,2,3,1,2,3]))#test fctionnemnt deck_mix_first


#pioche des cartes dans le deck

def pioche(deck,main_joueur,nb_carte):

    i=0
    
    for i in range(nb_carte):

        main_joueur.append(deck[i]) #ajout des cartes du deck dans la main du joueur

    return main_joueur

#print(pioche(deck=[1,2,3,4,5,6,7,8,9,10],main_joueur=[11,12,13,14,15,16],nb_carte=10))


#melange du deck 

def deck_mix(deck):
	
	deck_melanger=[]#definition deck melanger 
	r=0
	i=0
	cpt=len(deck)
	#transfert de carte aleatoirement dans le deck melanger
	for  i in range(cpt):
		
		r=random.randint(0,len(deck)-1)#nb aleatoire entre 0 et la derniere case du deck de depart 
		deck_melanger.append(deck[r])#deplacement de la carte dans le deck intermediaire
		del (deck[r])#supression de la carte transferee
	return deck_melanger

#print(deck_mix(deck=[1,2,3,4,5,6]))#test fonctionnement fct deck_mix


#envoie carte de la main vers les cartes posee

def hand_to_game(main,cartes_posee,card):
	
	i=0
	
	while main[i].idCarte != card.idCarte:
	
		i=i+1
		
	cartes_posee.append(main[i])
	del(cartes_posee[i])
	
	main_cartes_posee={'main':main,'cartes_posee':cartes_posee}#tableau de hachage contenant la main du joueur et les cartes posees
	
	return main_cartes_posee #retour de la main et des cartes posees
	

#envoie carte d'un repertoire vers le cimetiere

def cimetiere(cards_list,cimetiere,card):
	
	i=0
	
	while cards_list[i].idCarte != card.idCarte:
	
		i=i+1
		
	cimetiere.append(card_list[i])
	del(cards_list[i])
	
	cards_list_cimetiere={'cards_list':cards_list,'cimetiere':cimetiere}#tableau de hachage contenant le repertoire de la carte et le cimetiere
	
	return cards_list_cimetiere #retour du repertoire de la carte et du cimetiere


#envoie carte du cimetiere vers un repertoire

def cimetiere_to_list(card_destination,cimetiere,card):
	
	i=0
	
	while cimetiere[i].idCarte != card.idCarte:
	
		i=i+1
		
	card_destination.append(cimetiere[i])
	del(cimetiere[i])
	
	card_destination_cimetiere={'card_destination':cards_destination,'cimetiere':cimetiere}#tableau de hachage contenant le repertoire de destination de la carte et le cimetiere
	
	return cards_destination_cimetiere #retour du repertoire de destination la carte et du cimetiere



#Aptitude_Missionaire quand la carte entre jeu le joueur a +4 pdv

def Aptitude_Missionaire(joueur):
	
	joueur.pointDeVie=joueur.pointDeVie+4
	
	return (joueur)



