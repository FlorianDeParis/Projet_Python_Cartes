class creature(carte): #declaration class
    # célérité  -> n'est pas sujet au mal d'invocation.
    # vol       -> la creature acquier le vol et ne peut etre bloqué que par des créature qui ont le vol.
    # distortion -> la creature acquier la distortion et ne peut bloqué et etre bloqué que par des créature qui ont la distortion.
    # provocation -> permet a la créature attaquante de forcer une créature de l'adversaire a bloquer celle ci.
    # peur -> ne peut etre bloquée que par des créatures noires.
    # contact mortel -> lors d'une attaque la créature bloqueuse meurt.
    # lien de vie -> le propriétaire de la créature récupere autant de point de vie que de point de dégat infligé par cette créature.
    # initiative -> attaque en premier et ne subit donc pas de dommage dans le cas de créature de force egal.
    # equitation -> la creature ne peut etre bloqué que par des creature qui ont equitation, en revanche elle peut bloquer les creature avec et sans equitation.
    # double initiative -> inflige des dommage avec l'initiative plus un round de combat normal avec la creature defensive.
    #
    # piétinement -> une fois qu'elle a infligé suffisamment de blessures pour détruire tous ses bloqueurs, elle inflige les blessures restantes au joueur défenseur.
    # la flétrissure -> Les blessures infligées à une créature par une source avec la flétrissure ne sont pas marquées sur cette créature. À la place, autant de marqueurs -1/-1 sont mis sur la créature
    # indestructibilité -> Si un permanent est indestructible, les règles et les effets ne peuvent pas le détruire. Des règles ou des effets peuvent faire qu'un permanent indestructible soit sacrifié, mis dans un cimetière ou retiré de la partie.
    # intimidation -> Elle ressemble énormément à la peur, à la différence près qu'elle s'adapte à la (aux) couleur(s) de la créature qui la porte.
    # débordement -> Cette capacité, attaquante avant tout, consiste à faire perdre -1/-1 à toutes les créatures sans le débordement désignées pour bloquer une créature avec le débordement
    
    
    
    def __init__(self, vie, degat):#constructeur
        self.vie = vie
        self.degat = degat
        self.caracteristique = []