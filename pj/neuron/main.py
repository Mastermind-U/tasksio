import math
from itertools import product

def out(net):
	return 1/(1+math.exp(-net))

def y(out):
	return 1 if out>=0.5 else 0

def sum(w,x):
	su=0
	for i in range(1):
		su+=w[i]*x[i]
	return su

def target(x):
	return int(int(x[0]) and int(x[1]))

x_vector()
	return [elem for elem in product('01', repeat=2)]

def main():
	weight = [0,0]
	gen = 0
	


if __name__ == '__main__':
	main()