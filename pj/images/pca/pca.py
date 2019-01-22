from numpy import *
from PIL import Image
from pylab import *
import os

def get_imlist(path):
	return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]

def pca(x):

	num_data, dim = x.shape

	mean_x = x.mean(axis=0)
	x = x - mean_x

	if dim > num_data:

		M = dot(x, x.T) # Ковариационная матрица
		e, EV = linalg.eigh(M) # Собственные значения и Собственные векторы
		tmp = dot(x, EV).T #Это и есть компактный трюк
		V = tmp[::1] # меняем порядок потому что нам нужны последние собственные векторы

		S = sqrt(e)[::-1] # меняем порядок потому что собственные значения-по возрастанию

		for i in range(V.shape[1]):
			V[:, i] /= S

	else:
		# МГК (метод главных компонент) с использованием сингулярного разложения:
		U, S, V = linalg.svd(x)
		V = V[:num_data] # первые num_data строк
		# возвращаем матрицу проекции, дисперсию и среднее
	return V, S, mean_x


def main():
	imlist = get_imlist('../learning')

	im = array(Image.open(imlist[0]))
	m,n = im.shape[0:2]
	imnbr = len(imlist)
	immatrix = array([array(Image.open(imname)).flatten() for imname in imlist], 'f')
	# immatrix = array([array(Image.open(im)).flatten() for im in imlist], 'f')
	V, S, immean = pca(immatrix)
	figure()
	gray()
	subplot(2,4,1)
	imshow(immean.reshape(m,n))
	for i in range(7):
		subplot(2,4,i+2)
		imshow(V[i].reshape(m,n))
	show()



if __name__ == '__main__':
	main()

