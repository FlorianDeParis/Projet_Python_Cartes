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
#carte type monstre: 
        if deck[i]==1 or deck[i]==2 :#carte type sort
            deck_inter_monstre_sort.append(deck[i])#deplacement de la carte
        elif deck[i]==3 :#carte de type terrain
            deck_inter_terrain.append(deck[i])
    cpt_t=len(deck_inter_terrain)
    cpt_m_s=len(deck_inter_monstre_sort)
    rep_ct_t=cpt_m_s//cpt_t
    i=0
    while (len(deck_inter_terrain)>0)and(len(deck_inter_monstre_sort)>0):
        for i in range(rep_ct_t):
           r=random.randint(0,len(deck_inter_monstre_sort)-1)
           deck_melanger.append(deck_inter_monstre_sort[r])
           del (deck_inter_monstre_sort[r])

        r=random.randint(0,len(deck_inter_terrain)-1)
        deck_melanger.append(deck_inter_terrain[r])

    return deck_melanger

print(deck_mix_first(deck=[1,2,3,1,2,3,1,2,3,1,2,3]))
