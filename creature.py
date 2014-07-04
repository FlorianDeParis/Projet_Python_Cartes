from carte import*
class creature(carte): #declaration class
    #---------------DEFENSE----------------
 # vol    -> la creature acquier le vol et ne peut etre bloque que par des creature qui ont le vol.
 # distortion -> la creature acquier la distortion et ne peut bloque et etre bloque que par des creature qui ont la distortion.
  # peur -> ne peut etre bloquee que par des creatures noires.
  # equitation -> la creature ne peut etre bloque que par des creature qui ont equitation, en revanche elle peut bloquer les creature avec et sans equitation.
  # intimidation ->Elle ressemble enormement a la peur, a la difference pres quelle s adapte a la (aux) couleur(s) de la creature qui la porte.
  # imblocable -> ne peux pas etre bloque par une creature
  
  
  #--------------- SELECTION CARTE ----------------
  # celerite -> n'est pas sujet au mal d'invocation.
  
  #---------------ATTAQUE----------------
  # contact mortel -> lors d'une attaque la creature bloqueuse meurt.
  
  
  
  
  # initiative -> attaque en premier et ne subit donc pas de dommage dans le cas de creature de force egal.
  
  # double initiative -> inflige des dommage avec l'initiative plus un round de combat normal avec la creature defensive.
  
  # debordement -> Cette capacite, attaquante avant tout, consiste a faire perdre -1/-1 a toutes les creatures sans le debordement designees pour bloquer une creature avec le debordement
  
  # pietinement -> une fois qu'elle a inflige suffisamment de blessures pour detruire tous ses bloqueurs, elle inflige les blessures restantes au joueur defenseur.
  
  # indestructible -> Si un permanent est indestructible, les regles et les effets ne peuvent pas le detruire. Des regles ou des effets peuvent faire qu'un permanent indestructible soit sacrifie, mis dans un cimetiere ou retire de la partie.
  
  
  
  # lien de vie -> le proprietaire de la creature recupere autant de point de vie que de point de degat inflige par cette creature.
  
  
  #---------------MISE DE COTE----------------
  # provocation -> permet a la creature attaquante de forcer une creature de l'adversaire a bloquer celle ci.
  # (on va le mettre de cote pour le moment chiant a coder)
  #lafletrissure->les blessures infligees a une creature par une source avec la fletrissure ne sont pas marquees sur cette creature. a la place, autant de marqueurs -1/-1 sont mis sur la creature (attention dur a gerer ne pas prendre florian)
  
  
  def __init__(self, nomCarte, idCarte, url_img, couleurCarte,vie, degat,caracteristique):#constructeur
    carte.__init__(self, nomCarte, idCarte, url_img, couleurCarte)
    self.vie = vie
    self.degat = degat
    self.caracteristique = []
    self.mal_invocation = 1