from numpy import *
from PIL import Image
from pylab import *
from imtools import histeq
# im = array(Image.open('emp.jpg'))

# imshow(im)
# print('Щелкните в 3х точках: ')
# x = ginput(3)
# print('', x)
# show()

im = array(Image.open('emp.jpg').convert('L'))
im2, cdf = histeq(im)
figure()
axis('off')
imshow(im)
# contour(im, origin = 'image')


figure()
imshow(im2)


figure()
hist(im.flatten(), 128)

figure()
hist(im2.flatten(), 128)
show()