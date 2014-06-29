#pioche des cartes dans le deck

def pioche(deck,main_joueur,nb_carte):

    i=0
    
    for i in range(nb_carte):

        main_joueur.append(deck[i]) #ajout des cartes du deck dans la main du joueur

    return main_joueur

#print(pioche(deck=[1,2,3,4,5,6,7,8,9,10],main_joueur=[11,12,13,14,15,16],nb_carte=10))
