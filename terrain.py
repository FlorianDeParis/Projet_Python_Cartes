from carte import*
class terrain(carte): #declaration class
    

    def __init__(self ,nomCarte, idCarte, url_img, couleurCarte,mana):#constructeur
        carte.__init__(self, nomCarte, idCarte, url_img, couleurCarte)
	self.mana = {   'blanc' :  0
                        ,'rouge' :  0
                        ,'noir'  :  0
                        ,'bleu'  :  0
                        ,'vert'  :  0}
# tableau indiquant la quantite de quelle mana le terrain retourne