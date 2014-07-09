class carte: #declaration class
    # !!! attention ne pas oublier que lors de la creation d un deck les carte selectionner iront directement dans bibliotheque du joueur.
    # !!! en revanche dans le cas ou l on veut proposer des deck tout fait on se basera sur une table en plus dans la base

    def __init__(self, nomCarte, idCarte, url_img, couleurCarte):#constructeur
        self.nomCarte = nomCarte
        self.idCarte = idCarte
        self.url_img = url_img
        self.couleurCarte = couleurCarte
        self.x = 0
        self.y = 0
        self.coutInvocation = {  'blanc'     :  0
                                ,'rouge'     :  0
                                ,'noir'      :  0
                                ,'bleu'      :  0
                                ,'vert'      :  0
                                ,'incolore'  :  0}
# ce tableau represente les cout d invocation de chaque carte. Il sera compare au tableau  pointMana  du joueur pour voir si le joueur a payer suffisement de mana pour l invocation. On traiterai l incolore en dernier car il s agit de payer avec n importe qu elle couleur de notre choix
#maCarte = carte("cauchemard", 10, "ecureuil", "rouge")
