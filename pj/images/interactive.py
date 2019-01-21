from PIL import Image
from pylab import *

# im = array(Image.open('emp.jpg'))

# imshow(im)
# print('Щелкните в 3х точках: ')
# x = ginput(3)
# print('', x)
# show()


def imresize(im, size):
	pil_im = Image.formarray(uint8(im))
	return array(pil_im.resize(sz))

def histeq(im, nbr_bins=256):
	# Гистограмма полутонового изображения

	imhist, bins = histogram(im.flatten(), nbr_bins, normed=True)
	cdf = imhist.cumsum()
	cdf = 255 * cdf / cdf [-1] #Нормируем
	im2 = interp(im.flatten(), bins[:-1], cdf)
	return im2.reshape(im.shape), cdf