def Aptitude_Missionnaire(joueur):   
		# Quand le Missionnaire solitaire arrive sur le champ de bataille, vous gagnez 4 points de vie.
		joueur.vie= joueur.vie + 4
		return joueur

def Poison_ardent(joueur):
   #~ # Quand la creature arrive sur le champ de bataille, les creatures que vos adversaires controlent ...
	#~ #gagnent-2/-2jusqu'alafindutour.
	array_cartePose = joueur.cartePose
	for allmonstre in array_cartePose:
		if allmonstre.type ==2:
			
