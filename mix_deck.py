#melange du deck 
import random
deck=[1,2,3,4,5]
#def deck_mix(deck):
deck_inter=[] 
i=0
for i in range(4):
	r = random.randint(1,length(deck_inter)-1)
	deck_inter[i]=deck[r]
	del deck[r]
	#return deck_inter
print(deck_inter)
