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
    
    
    
    
    def __init__(self, vie, degat):#constructeur
        self.vie = vie
        self.degat = degat
        self.caracteristique = []