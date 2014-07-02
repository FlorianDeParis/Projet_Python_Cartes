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
#fonction pour savoir si un joueur est mort ou non FAITE
    #objet joueur passe en paramettre
    # lie au point de vie et a la taille de la bibliotheque une fois a 0 on meurt

#fonction pour piocher des cartes FAITE
    #le nombre de carte a piocher passer en paramettre 

#fonction compter si la main est superieur a 7 ou non
    #objet joueur passe en parametre

#multiple fonction qui passe une carte d'une liste a une autre
    # on passe une carte en paramettre
    # biblioteque -> main
    # bibliotheque -> cimetiere
    # main -> carte_pose
    # main -> cimetiere
    # cimetiere -> carte_pose
    # cimetiere -> main
    # carte_pose -> cimetiere
    # carte_pose -> carte engage (attention la ce n'est pas un deplacement mais une copie)

<<<<<<< HEAD
    #fonction qui test si un terrain a ete pose ou non pendant ce tour
        # recoit un objet joueur

    #fonction qui test si une carte est engage ou non
        # recoit un objet carte
=======
#fonction qui test si un terrain a été posé ou non pendant ce tour
    # recoit un objet joueur

#fonction qui test si une carte est engagé ou non
    # recoit un objet carte
>>>>>>> ccc82d155db4e54af64d5091e0b27cf5318f5334

#fonction pour melanger le deck de fa�on organisee pour le premier tour FAITE

<<<<<<< HEAD
#fonction pour  melanger le deck FAITE

#fonction pour chercher et deplacer carte dans le deck FAITE

#fonction pour modifier la vie et les degats d'un monstre FAITE

#fonction qui verifie si un objet creature peut jouer ou pas "mal d'invocation"

=======
#fonction qui verifie si un objet créature peut jouer ou pas "mal d'invocation"
>>>>>>> ccc82d155db4e54af64d5091e0b27cf5318f5334

#fonction qui verifie si un sort peut etre jouer a ce moment cad
    #ephemere nimporte quand
    #rituel seulement pendant la phase de pose
    #enchantement seulement pendant la phase de pose mais reste sur le terrain

#fonction qui parcour les enchantement sur le terrain et les executes directement sur leurs cibles pour quil soient appliquer en premier


#fonction qui recoit un objetSort et un objJouer et verifie si le joueur a engager suffisement de mana vis a vis du cout dinvocation attention pour les mana incolor prendre ce qui reste apres avoir tout deduit et retourner true ou false








if __name__ == "__main__":
    main() # L'appel à la fonction main