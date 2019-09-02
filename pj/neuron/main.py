import math
from itertools import product

import matplotlib.pyplot as plt


#График
def plot(x, y):
	fig, ax = plt.subplots(figsize=(4, 4))
	ax.stackplot(x, y, labels=['Dynamics'], colors=['c'])

	ax.scatter(x=x, y=y, marker='s', c='g')
	ax.set_title('Education process')
	ax.set_xlabel('$Epochs$')
	ax.set_ylabel('$Err$')
	ax.legend(loc='upper left')
	fig.tight_layout()

	plt.show()


def net(w,x):
	return sum(w[i] * int(x[i]) for i in range(2))

def out(net):
	# net=0	#Считаем net
	# for i in range(2):
	# 	net+=int(w[i])*int(x[i])
	# 	print(f'w: {w[i]}, x :{x[i]}, net: {net}')
	# net = sum(w[i] * int(x[i]) for i in range(2))
	#возвращаем 1 или 0 в зависимости от вывода функции активации
	return 1 if net>=0.5 else 0

def target(x): #вычисления конъюнкции
	return int(int(x[0]) and int(x[1]))

def x_vectors(): #генератор комбинации таблицы истинности
	return [elem for elem in product('01', repeat=2)]

def f_vector(): #выводим результат конъюнкции по таблице с иксами
	return [target(vector) for vector in x_vectors()]



def main():
	weight = [0.0, 0.0] #начальные веса
	y = [0, 0, 0, 0] #инициализация массива вывода
	gen = 0 #Поколение
	error = 100
	nu = 0.04
	gen_arr = error_arr = []
	while error != 0:  #error != 0: #gen<20: #
		error = 0
		print(f'Эпоха: {gen}')
		for i,x in enumerate(x_vectors()):
			net_n = net(weight, x)
			y[i] = out(net_n)

			delta = f_vector()[i] - y[i]
			# err = f_vector()[i] - net_n
			error += 1 if delta != 0 else 0
			#отладка
			# for j in range(2):
			# 	print(f'{weight[j]} + {nu} * {delta} * {x[j]} = ', [weight[l] + nu * delta * int(x[l]) for l in range(2)][j])

			#модификация весов
			weight = [weight[l] + nu * delta * int(x[l]) for l in range(2)]
			#тоже отладка
			print(f'x: {x}, f: {f_vector()[i]}, y:{y[i]}, w:{weight}, error: {error}, delta: {delta}')
		print('------------------------')
		gen += 1
		gen_arr.append(gen)
		error_arr.append(error)



	plot(gen_arr, error_arr)
	print(f'\nКоличество эпох: {gen}')
	print(f'Конечный вес: {weight}')

if __name__ == '__main__':
	main()