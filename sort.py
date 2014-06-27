class sort(carte): #declaration class
    

    def __init__(self):#constructeur
        self.idSort = idSort
        self.type=type
        self.cibleSort = {  'cible'     =  0
                            ,'creature' =  0
                            ,'joueur'   =  0
                            }
 # ce tableau va permettre de savoir ce que peut cibler le sortilege, et donc de limiter dans le graphisme les débordements
# il y aura un switch case pour attribuer un id