#envoie carte du cimetiere vers un repertoire

from carte import*

def cimetiere_to_list(card_destination,cimetiere,card):
	
	i=0
	
	while cimetiere[i].idCarte != card.idCarte:
	
		i=i+1
		
	card_destination.append(cimetiere[i])
	del(cimetiere[i])
	
	card_destination_cimetiere={'card_destination':cards_destination,'cimetiere':cimetiere}#tableau de hachage contenant le repertoire de destination de la carte et le cimetiere
	
	return cards_destination_cimetiere #retour du repertoire de destination la carte et du cimetiere
	
	