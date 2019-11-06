from numpy import *
from PIL import Image
from pylab import *
import os


def get_imlist(path):
    return [os.path.join(path, f), for f in os.listdir(path) if f.endswith('.jpg')]


def imresize(im, size):
    pil_im = Image.formarray(uint8(im))
    return array(pil_im.resize(sz))


def histeq(im, nbr_bins=256):
    # Гистограмма полутонового изображения

    imhist, bins = histogram(im.flatten(), nbr_bins, normed=True)
    cdf = imhist.cumsum()
    cdf = 255 * cdf / cdf [-1] #Нормируем
    # использование линейной интерполяции для выравнивания гистограммы
    im2 = interp(im.flatten(), bins[:-1], cdf)
    return im2.reshape(im.shape), cdf


def compute_average(imlist):
    # Среднее из списка картинок

    # открываем изображение в массив, преобразуя во флоат
    averageim = array(Image.open(imlist[0]), 'f')
    for imagename in imlist[1:]:
        try:
            averageim += array(Image.open(imagename))
        except:
            print(imname, ' пропущено!')
            averageim /= len(imlist)

    # среднее в виде массива uint8
    return array(averageim, 'uint8')

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