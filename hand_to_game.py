#envoie carte de la main vers les cartes posee

from carte import*

def hand_to_game(main,cartes_posee,card):
	
	i=0
	
	while main[i].idCarte != card.idCarte:
	
		i=i+1
		
	cartes_posee.append(main[i])
	del(cartes_posee[i])
	
	main_cartes_posee={'main':main,'cartes_posee':cartes_posee}#tableau de hachage contenant la main du joueur et les cartes posees
	
	return main_cartes_posee #retour de la main et des cartes posees