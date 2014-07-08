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

  #def Renfort_1():
    # Créature possédant cette aptitude d'origine: Garde Moustique
    # Coût d'exploitation: 1 générique + 1 blanc
    # Description: défaussez-vous de cette carte: Mettez un marqueur +1/+1 sur la créature ciblée

  #def Escadron():
    # SORT GENERIQUE
    # Créature possédant cette aptitude d'origine: Faucon d'escadron
    # Description: Quand la créature arrive sur le champ de bataille, vous pouvez chercher dans votre bibliothèque jusqu'à trois cartes identiques ...
    # ... les révéler, les mettre dans votre main, puis mélanger votre bibliothèque.

  #def Aptitude_Missionnaire():  FAIT
    # Créature possédant cette aptitude d'origine: Missionnaire Solitaire
    # Quand le Missionnaire solitaire arrive sur le champ de bataille, vous gagnez 4 points de vie.

  #def Toucheterre():
    # SORT GENERIQUE
    # Créature possédant cette aptitude d'origine: Lynx des steppes
    # A chaque fois qu'un terrain arrive sur le champ de bataille sous votre contrôle, ...
    # ... la créature gagne +2/+2 jusqu'à la fin du tour.

  #def Affinite_pour_les_plaines():
    # Créature possédant cette aptitude d'origine: Golem de rasoirs
    # Description: Ce sort coûte (un générique) de moins à jouer pour chaque plaine que vous contrôlez.

  #def Art_des_metaux():
    # Créature possédant cette aptitude d'origine: Champion Gravé
    # Le champion gravé a la protection contre toutes les couleurs tant que vous contrôlez au moins trois artefacts.
  
  #def Regeneration():
    # Créature possédant cette aptitude d'origine: Troll à la trique
    # Coût d'exploitation: 1 vert
    # Description: regénérez le Troll à la trique (La prochaine fois que cette créature devrait être détruite ce tour-ci, elle ne l'est pas. ...
    # ... A la place, engagez-la, retirez-lui toutes ses blessures et retirez-la du combat.)

  #def Generation_de_terrain():
    # Créature possédant cette aptitude d'origine: Oracle de Mul Daya
    # Vous pouvez jouer un terrain supplémentaire pendant chacun de vos tours.

  #def Illusion():
    # Créature possédant cette aptitude d'origine: Oracle de Mul Daya
    # Jouez avec la carte du dessus de votre bibliothèque révélée.

  #def Dileme_de_l_oracle():
    # Créature possédant cette aptitude d'origine: Oracle de Mul Daya
    # Vous pouvez jouer la carte du dessus de votre bibliothèque si c'est une carte de terrain.

  #def Barriere_de gaia():
    # Créature possédant cette aptitude d'origine: La Vengeance de Gaia
    # La Vengeance de Gaia ne peut pas être la cible de sorts non-verts ou de capacités de sources non-vertes.

  #def Desillusion_inevitable():
    # Créature possédant cette aptitude d'origine: La Vengeance de Gaia
    # La Vengeance de Gaia pas être contrecarée

  #def Oeil_pour_oeil():
    # Créature possédant cette aptitude d'origine: Messager interville
    # A chaque fois que la Messager interville inflige des blessures de combat à un joueur, ce joueur met autant de cartes... 
    # ... du dessus de sa bibliothèque dans son cimetière

  #def Reincarnation_magique():
    # Créature possédant cette aptitude d'origine: Archéomancienne
    # Quand l'Archéomancienne arrive sur le champ de bataille, renvoyer une carte d'éphémère ou de rituel ciblée ...
    # ... depuis votre cimetière dans votre main.

  #def Destin_maccabre():
    # Créature possédant cette aptitude d'origine: Phantasme de Jace
    # La créature gagne +4/+4 tant qu'un adversaire a au moins dix cartes dans son cimetière.

  #def Amelioration():
    # SORT GENERIQUE
    # Créature possédant cette aptitude d'origine: Chronomate
    # Coût d'exploitation: 1 générique + (flèche retournée?)
    # Description: Mettez un marqueur +1/+1 sur la créature.

  #def Poison_ardent():
    # Créature possédant cette aptitude d'origine: Guivre du massacre
    # Quand le Guivre du massacre arrive sur le champ de bataille, les créatures que vos adversaires contrôlent ...
    # ... gagnent -2/-2 jusqu'à la fin du tour.

  #def Malediction():
    # Créature possédant cette aptitude d'origine: Guivre du massacre
    # A chaque fois qu'une créature qu'un adversaire contrôle est mise dans un cimetière depuis ...
    # ... le champs de bataille, ce joueur perd 2 points de vie. 

  #def Destruction():
    # Créature possédant cette aptitude d'origine: Avatar du malheur
    # Conditions: (flêche retournée?)
    # Description: Détruisez la créature ciblée. Elle ne peut pas être regénérée.

  #def Engagement():
    # Créature possédant cette aptitude d'origine: Messager de Geralf
    # Le Messager de Geralf arrive sur le champ de bataille engagé.

  #def Ligne_de_mire():
    # Créature possédant cette aptitude d'origine: Messager de Geralf
    # Quand le Messager de Geralf arrive sur le champ de bataille, l'adversaire ciblé perd 2 points de vie.

  #def Absorption():
    # Créature possédant cette aptitude d'origine: Oblitérateur phyrexian
    # A chaque fois qu'une source inflige des blessures à l'Oblitérateur phyrexian, le contrôleur de cette source ...
    # ... sacrifie autant de permanents.

  #def Mirroir():
    # Créature possédant cette aptitude d'origine: Mikaeus, le maudit
    # A chaque fois qu'un humain vous inflige des blessures, détruisez-le.

  #def Abime():
    # SORT GENERIQUE
    # Créature possédant cette aptitude d'origine: Excavenfer
    # Coût d'exploitation: 3 noirs + (flèche retournée?)
    # Description: Détruisez le terrain ciblé. Si ce terrain est non-base, dégagez la créature.

  #def Assombrissement():
    # SORT GENERIQUE
    # Créature possédant cette aptitude d'origine: Ombre nantuko
    # Coût d'exploitation: 1 noir
    # Description : La créature gagne +1/+1 jusqu'à la fin du tour.

  #def Sacrifice():
    # Créature possédant cette aptitude d'origine: Nattes, seide de la Coterie
    # Description: Au début de l'entretien de chaque joueur, ce joueur sacrifie un artefact, une créature ou un terrain.

  #def Terrain_boueux():
    # Créature possédant cette aptitude d'origine: Revenante des Nirkana
    # Description: A chaque fois que vous engagez un marais pour du mana, ajoutez (un noir) à votre réserve (en plus du mana produit par le terrain).
  
#~ # ce tableau va permettre de savoir ce que peut cibler le sortilege, et donc de limiter dans le graphisme les debordements
#~ # il y aura un switch case pour attribuer un id
