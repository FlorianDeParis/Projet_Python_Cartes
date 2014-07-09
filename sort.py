from carte import*
class sort(carte): #declaration class
    

	def __init__(self,nomCarte, idCarte, url_img, couleurCarte,idSort):#constructeur
		carte.__init__(self, nomCarte, idCarte, url_img, couleurCarte)
		self.idSort = idSort
		self.type=type
		self.cibleSort = {  'cible' :  0
                          ,'creature' : 0
                          ,'joueur'   :  0
                          }
  #///////fait dans fichier fonction ///////
  #~ def Renfort_1():
    #~ # Cout dexploitation: 1 generique + 1 blanc
    #~ # Description: defaussez-vous de cette carte: Mettez un marqueur +1/+1 sur la creature ciblee

  #~ def Vol():
    #~ # Quand la creature arrive sur le champ de bataille  vous pouvez chercher dans votre bibliotheque 
    #~ # jusqu a trois cartes les reveler les mettre dans votre main puis melanger votre bibliotheque

	 #///////fait dans fichier fonction ///////
	#def Aptitude_Missionnaire(joueur):   
		#~ Quand le Missionnaire solitaire arrive sur le champ de bataille, vous gagnez 4 points de vie.
		#joueur.vie= joueur.vie + 4
		#return joueur

  #~ def Toucheterre():
    #~ # A chaque fois qu'un terrain arrive sur le champ de bataille sous votre controle, ...
    #~ # la creature gagne +2/+2 jusqu'a la fin du tour.

  #~ def Art_des_metaux():
    #~ # Le champion grave a la protection contre toutes les couleurs tant que vous controlez au moins trois artefacts.

  #~ def Regeneration():
    #~ # Cout d'exploitation: 1 vert
    #~ # Description: regenerez la creature (La prochaine fois que cette creature devrait etre detruite ce tour-ci, elle ne l'est pas. ...
    #~ # ... A la place, engagez-la, retirez-lui toutes ses blessures et retirez-la du combat.)

  #~ def Generation_de_terrain():
    #~ # Vous pouvez jouer un terrain supplementaire pendant chacun de vos tours.

  #~ def Illusion():
    #~ # Jouez avec la carte du dessus de votre bibliotheque revelee.

  #~ def Parole_de_l_oracle():
    #~ # Vous pouvez jouer la carte du dessus de votre bibliotheque si c'est une carte de terrain.

  #~ def Celerite():
    #~ # La creature ne peut pas etre la cible de sorts non-verts ou de capacites de sources non-vertes.

  #~ def Desillusion_inevitable():
    #~ # La creature ne peut pas etre contrecaree

  #~ def Oeil_pour_oeil():
    #~ #A chaque fois que la creature inflige des blessures de combat a un joueur, ce joueur met autant de cartes...
    #~ # ... du dessus de sa bibliotheque dans son cimetiere

  #~ def Reincarnation_magique():
    #~ # Quand la creature arrive sur le champ de bataille, renvoyer une carte d'ephemere ou de rituel ciblee ...
    #~ # ... depuis votre cimetiere dans votre main.

  #~ def Destin_maccabre():
    #~ # La creature gagne +4/+4 tant qu'un adversaire a au moins dix cartes dans son cimetiere.

  #~ def Amelioration():
    #~ # Cout d'exploitation: 1 generique + (fleche retournee?)
    #~ # Description: Mettez un marqueur +1/+1 sur la creature.
 #///////fait dans fichier fonction ///////
  #~ def Poison_ardent():
    #~ # Quand la creature arrive sur le champ de bataille, les creatures que vos adversaires controlent ...
    #~ #gagnent-2/-2jusqu'alafindutour.
    
  #~ def Malediction():
    #~ # A chaque fois qu'une creature qu'un adversaire controle est mise dans un cimetiere depuis ...
    #~ # ... le champs de bataille, ce joueur perd 2 points de vie. 

  #~ def Destruction():
    #~ # Conditions: (fleche retournee?)
    #~ # Description: Detruisez la creature ciblee. Elle ne peut pas etre regeneree.
  
#~ # ce tableau va permettre de savoir ce que peut cibler le sortilege, et donc de limiter dans le graphisme les debordements
#~ # il y aura un switch case pour attribuer un id
