# Main
# lancement du jeu creation du graphique
# creation d'un joueur ou chargement joueur existant
# demande connection Resaux ou AI
# choix deck existant ou creation deck avec liste des cartes
# Lancement partie
#       ------------------
# Lancement boucle sur tableau joueur tant qu'il y a plus d'un joueur dedans
#   phase de desengagement (automatique)
#   phase de pioche (automatique) fct pioche faite
#   check si joueur est mort ou non (si oui on eleve le joueur du tableau et on    quitte le jeux)
#   choix du joueur pose ou non
#   si oui phase de pose
#   choix du joueur attaque ou non
#   si oui phase d'attaque
#   check si joueur est mort (si oui on eleve le joueur du tableau)
# Fin de boucle
#
# retour score
# incremente xp joueur
#
#
#
#
#
#
#
#
from connection import* 
def main():
    listeCarte = select_all_carte()
    listeDeck = []

#on charge au demarage toute les cartes
    #connexion bdd et retour des cartes de la base
    #boucle sur les resultats et on ceer un objet carte par resultat
    #   maCarte = carte()
    #   listeCarte.append(maCarte)
#on charge au demarage toute les cartes
    #connexion bdd et retour des deck de la base
    #on boucle sur les resultat et pour chaque deck on va chercher ses cartes
        #on creer un tableau comme listeCarte_indice  []
        #connexion bdd et retour des cartes du deck de la base
        #boucle sur les resultats et on ceer un objet carte par resultat
            #   maCarte = carte()
            #   listeCarte_indice.append(maCarte)
        #listeDeck.apend(listeCarte_indice)

#on affiche un panneaux pour choisir un perso ou en creer un






#-----------------------------------------------------------
"""faite"""
#fonction pour savoir si un joueur est mort ou non FAITE
    #objet joueur passe en paramettre
    # lie au point de vie et a la taille de la bibliotheque une fois a 0 on meurt

"""faite"""
#fonction pour piocher des cartes FAITE
    #le nombre de carte a piocher passer en paramettre 

"""faite"""
#fonction compter si la main est superieur a 7 ou non FAITE
    #objet joueur passe en parametre

#multiple fonction qui passe une carte d'une liste a une autre
    # on passe une carte en paramettre
    # biblioteque -> main FAITE? PIOCHE?
"""faite"""    # bibliotheque -> cimetiere FAITE
"""faite"""    # main -> carte_pose FAITE
"""faite"""    # main -> cimetiere FAITE
"""faite"""    # cimetiere -> carte_pose FAITE
"""faite"""    # cimetiere -> main FAITE
"""faite"""    # carte_pose -> cimetiere FAITE

# carte_pose -> carte engage (attention la ce n'est pas un deplacement mais une copie)

#fonction qui test si un terrain a ete pose ou non pendant ce tour
    # recoit un objet joueur

#fonction qui test si une carte est engage ou non
    # recoit un objet carte

"""faite"""
#fonction pour melanger le deck de façon organisee pour le premier tour FAITE

"""faite"""
#fonction pour  melanger le deck FAITE

"""faite"""
#fonction pour chercher et deplacer carte dans le deck FAITE

"""faite"""
#fonction pour modifier la vie et les degats d'un monstre FAITE

#fonction qui verifie si un objet creature peut jouer ou pas "mal d'invocation"













if __name__ == "__main__":
    main() # L'appel Ã  la fonction main