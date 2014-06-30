#melange orgainse du deck pour le debut de partie
import random
from creature import*
from sort import*
from terrain import*
def deck_mix_first(deck):
	
    deck_inter_monstre_sort=[]#deck intermediaire pour stocker les cartes monstre et sort
    deck_inter_terrain=[]#deck intermediaire pour stocker les cartes terrain
    deck_melanger=[]
    r=0
    i=0
    cpt=len(deck)#compteur de cartes dans le deck
    
    for i in range(cpt):

        if (type(deck[i]) is creature) or (type(deck[i])is sort) :#carte type monstre et sort (provisoir en attente de la méthode d'identification des 
            deck_inter_monstre_sort.append(deck[i])#deplacement de la carte
        elif type(deck[i]) is terrain :#carte de type terrain
            deck_inter_terrain.append(deck[i])
            
    cpt_t=len(deck_inter_terrain)#compteur carte terrain
    cpt_m_s=len(deck_inter_monstre_sort)#compteur carte monstre et sort
    rep_ct_t=cpt_m_s//cpt_t#calcule de l'alternance avec les carte terrrain
    i=0
    
    while (len(deck_inter_terrain)>0)and(len(deck_inter_monstre_sort)>0):
        
        for i in range(rep_ct_t): #deplacement des carte monstre et terrain dans le deck
           r=random.randint(0,len(deck_inter_monstre_sort)-1)
           deck_melanger.append(deck_inter_monstre_sort[r])
           del (deck_inter_monstre_sort[r])

        #deplacement des cartes terrain dans le deck
        r=random.randint(0,len(deck_inter_terrain)-1)
        deck_melanger.append(deck_inter_terrain[r])

    return deck_melanger

#print(deck_mix_first(deck=[1,2,3,1,2,3,1,2,3,1,2,3]))#test fctionnemnt deck_mix_first
