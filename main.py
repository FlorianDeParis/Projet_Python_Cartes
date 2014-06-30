# Main
# lancement du jeu creation du graphique
# creation d'un joueur ou chargement joueur existant
# demande connection Resaux ou AI
# choix deck existant ou création deck avec liste des cartes
# Lancement partie
#       ------------------
# Lancement boucle sur tableau joueur tant qu'il y a plus d'un joueur dedans
#   phase de désengagement (automatique)
#   phase de pioche (automatique)
#   check si joueur est mort ou non (si oui on eleve le joueur du tableau et on    quitte le jeux)
#   choix du joueur pose ou non
#   si oui phase de pose
#   choix du joueur attaque ou non
#   si oui phase d'attaque
#   check si joueur est mort (si oui on eleve le joueur du tableau)
# Fin de boucle
#
# retour score
# incrémente xp joueur
#
#
#
#
#
#
#
#

def main():
    listeCarte = []
    listeDeck = []

#on charge au démarage toute les cartes
    #connexion bdd et retour des cartes de la base
    #boucle sur les resultats et on ceer un objet carte par resultat
    #   maCarte = carte()
    #   listeCarte.append(maCarte)
#on charge au démarage toute les cartes
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
#fonction pour savoir si un joueur est mort ou non
    #objet joueur passé en paramettre
    # lié au point de vie et a la taille de la bibliotheque une fois a 0 on meurt

#fonction pour piocher des cartes
    #le nombre de carte a piocher passer en paramettre

#fonction compter si la main est supérieur a 7 ou non
    #objet joueur passé en parametre

#multiple fonction qui passe une carte d'une liste a une autre
    #on passe une carte en paramettre
    # biblioteque -> main
    # bibliotheque -> cimetiere
    # main -> carte_pose
    # main -> cimetiere
    # cimetiere -> carte_pose
    # cimetiere -> main
    # carte_posé -> cimetiere
    # carte_pose -> carte engagé (attention la ce n'est pas un déplacement mais une copie)



if __name__ == "__main__":
    main() # L'appel à la fonction main