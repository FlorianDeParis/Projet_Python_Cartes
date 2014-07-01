#import sys
#sys.path.append("home/pi/Desktop/Projet_Python_Cartes/")
from carte import *


import search_and_move



carte1= carte("carte1",1,"test1","couleur1")
carte2= carte("carte2",2,"test2","couleur2")
carte3= carte("carte3",3,"test3","couleur3")
carte4= carte("carte4",4,"test4","couleur4")
carte5= carte("carte5",5,"test5","couleur5")
carte6= carte("carte6",6,"test6","couleur6")

deck=[carte1,carte2,carte3,carte4,carte5,carte6]

print(search_and_move(deck=deck,card_ID=carte1.idCarte,position=5))

