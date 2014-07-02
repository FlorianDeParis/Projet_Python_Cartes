#60 ingeniosite de jace pioche 3 carte
from fct_pioche import*
def ingeniosite_de_jace(main_joueur,deck):
	
	main_joueur_final=[]
	
	main_joueur_final=pioche(deck,main_joueur,3)
	
	return main_joueur_final


#print(ingeniosite_de_jace([1,2,3,4,5,6],[7,8,9,10,11,12]))
