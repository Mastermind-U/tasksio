from numpy import *
from PIL import Image
from pylab import *
im = array(Image.open('emp.jpg').convert('L'))
im2 = 255 - im
im3 = (100.0/255) * im + 100
im4 = 255.0 * (im/255.0)**2


imshow(im4)
show()
print(int(im.min()), int(im.max()))