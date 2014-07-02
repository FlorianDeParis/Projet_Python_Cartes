from creature_carac_modif import*
from fct_pioche import*

#60 ingeniosite de jace pioche 3 carte
def ingeniosite_de_jace(main_joueur,deck):
	
	main_joueur_final=[]
	
	main_joueur_final=pioche(deck,main_joueur,3)
	
	return main_joueur_final

#print(ingeniosite_de_jace([1,2,3,4,5,6],[7,8,9,10,11,12]))

#25_raise_the_alarm ajoute 1/1 a une creature
def raise_the_alarm(creature):
	
	creature=creature_carac_modif(creature,1,1)
	
	return creature
	
#52_ecurage_de_pensee envoi 2 premieres cartes du deck dans le cimetiere	
def ecurage_de_pensee(deck,cimetiere):
	
	i=0
	
	for i in range(3):#parcourt a 3 reprises le deck
		
		cimetiere.append(deck[0])#rajoute premiere carte du deck dans le cimetiere
		del(deck[0])#supprime la carte du deck
	deck_cimetiere={'deck':deck,'cimetiere':cimetiere}#tableau de hachage contenant le deck et le cimetiere
	return deck_cimetiere#retour du deck et du cimetiere
	
//~ all = ecurage_de_pensee([1,2,3,4,5,6],[])
//~ print(all['deck'])
//~ print(all['cimetiere'])