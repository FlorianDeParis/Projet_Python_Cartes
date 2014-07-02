#fonction pour check si le joueur est en vie

from joueur import*

def check_player_alive(joueur):
	
	if joueur.pointDeVie == 0:
		
		return TRUE
	
	else :
		
		return FALSE