
from carte import*

import search_and_move



carte1= carte("carte1",1,"test1","rouge")
carte2= carte("carte2",2,"test2","vert")
carte3= carte("carte3",3,"test3","noir")
carte4= carte("carte4",4,"test4","bleu")
carte5= carte("carte5",5,"test5","noir")
carte6= carte("carte6",6,"test6","vert")

deck=[carte1,carte2,carte3,carte4,carte5,carte6]


print(search_and_move(deck=deck,card=carte2,position=5))


