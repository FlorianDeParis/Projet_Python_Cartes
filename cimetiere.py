#envoie carte d'un repertoire vers le cimetiere

from carte import*

def cimetiere(cards_list,cimetiere,card):
	
	i=0
	
	while cards_list[i].idCarte != card.idCarte:
	
		i=i+1
		
	cimetiere.append(card_list[i])
	del(cards_list[i])
	
	cards_list_cimetiere={'cards_list':cards_list,'cimetiere':cimetiere}#tableau de hachage contenant le repertoire de la carte et le cimetiere
	
	return cards_list_cimetiere #retour du repertoire de la carte et du cimetiere
	
	