#52_ecurage_de_pensee envoi 2 premieres cartes du deck dans le cimetiere

def ecurage_de_pensee(deck,cimetiere):
	
	i=0
	
	for i in range(3):#parcourt a 3 reprises le deck
		
		cimetiere.append(deck[0])#rajoute premiere carte du deck dans le cimetiere
		del(deck[0])#supprime la carte du deck
	deck_cimetiere={'deck':deck,'cimetiere':cimetiere}#tableau de hachage contenant le deck et le cimetiere
	return deck_cimetiere#retour du deck et du cimetiere
	
'''all = ecurage_de_pensee([1,2,3,4,5,6],[])
print(all['deck'])
print(all['cimetiere'])'''