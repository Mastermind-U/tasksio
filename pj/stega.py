from PIL import Image, ImageDraw



img  = Image.open("pil_color.png")
pix  = img.load()
w, h = img.size
keys = []


for i in range(10,w,90):
	keys.append([chr(elem) for elem in pix[(i,20)][:3]])

print(''.join(sum(keys, [])))

