import itertools 
a  = itertools.combinations_with_replacement([1,2,3,4,5],3)

for elem in a:
	password = ''
	for e in elem:
		password += str(e)
