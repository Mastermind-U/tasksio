import math
from itertools import product
from plot import plot




def out(w,x):
	net=0	#Считаем net
	for i in range(1):
		net+=int(w[i])*int(x[i])
	#выводим 1 или 0 в зависимости от вывода функции активации
	return 1 if (1/(1+math.exp(-net)))>=0.5 else 0 

def target(x): #вычисления конъюнкции
	return int(int(x[0]) and int(x[1]))

def x_vectors(): #генератор комбинации таблицы истинности
	return [elem for elem in product('01', repeat=2)]

def f_vector(): #выводим результат конъюнкции по таблице с иксами
	return [target(vector) for vector in x_vectors()]



def main():
	weight = [0,0]
	y = [0, 0, 0, 0]
	gen = 0
	error = 1
	nu = 0.25
	gen_arr = error_arr = []
	while error != 0:
		error = 0
		for i,x in enumerate(x_vectors()):
			y[i] = out(weight, x)

			delta = f_vector()[i] - y[i]
			error += 1 if delta != 0 else 0

			weight = [weight[l] + nu * delta * int(x[l]) for l in range(1)]

		gen += 1
		gen_arr.append(gen)
		error_arr.append(error)
	plot(epoch_arr, error_arr)
	print(f'\nКоличество эпох: {gen}')
	print(f'Конечный вес: {weight}')

if __name__ == '__main__':
	main()