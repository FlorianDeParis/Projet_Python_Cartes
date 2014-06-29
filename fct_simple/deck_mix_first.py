#melange orgainse du deck pour le debut de partie
import random

def deck_mix_first(deck):
	
    deck_inter_monstre_sort=[]#deck intermediaire pour stocker les cartes monstre et sort
    deck_inter_terrain=[]#deck intermediaire pour stocker les cartes terrain
    deck_melanger=[]
    r=0
    i=0
    cpt=len(deck)
    for i in range(cpt):

        if deck[i]=='''carte type monstre:'''||deck[i]=='''carte type sort''':
            deck_inter_monstre_sort.append(deck[i])#deplacement de la carte
        elif deck[i]=='''carte de type terrain''':
                deck_inter_terrain.append(deck[i])
    
        
                    
                    
