
from carte import*

import search_and_move



carte1= carte("carte1",1,"test1","rouge")
carte2= carte("carte2",2,"test2","vert")
carte3= carte("carte3",3,"test3","noir")
carte4= carte("carte4",4,"test4","bleu")
carte5= carte("carte5",5,"test5","noir")
carte6= carte("carte6",6,"test6","vert")

deck=[carte1,carte2,carte3,carte4,carte5,carte6]

<<<<<<< HEAD
print(search_and_move(deck=deck,card_ID=2,position=5))
=======
print(search_and_move(deck=deck,card=carte2,position=5))
'''

from carte import *
#from joueur import *
#import carte

#monJoueur = joueur(12,"lio",20,100)
maCarte = carte("cauchemard", 10, "ecureuil", "rouge")
>>>>>>> 4d3901ec673bfa8f899a5c2f0f2f43552be90715

print(type(maCarte) is carte)
#print(type(maCarte) is joueur)'''
