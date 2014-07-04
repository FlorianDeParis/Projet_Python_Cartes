from carte import*
from creature import*
from sort import*

def test_type(type):
	
	a=0
	
	if type=="creature":
		a=creature()
		
	elif type=="sort":
		a=sort()
	return a
	
print(type(creature))
print(type(sort))
	
	
	