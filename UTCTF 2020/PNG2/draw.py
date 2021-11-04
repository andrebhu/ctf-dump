import PIL
from PIL import Image
o = open("pic.png2", "rb")
size = 1487, 648
im = PIL.Image.new(mode = "RGB", size =size)
pixels = o.read()[21:]
pixels = [pixels[i:i+3] for i in range(0, len(pixels), 3)]
edit = im.load()
count = 0
print(hex(pixels[0][0]))
for j in range(im.size[1]):
	for i in range(im.size[0]):	
		edit[i, j] = (int(hex(pixels[count][0]), 16), int(hex(pixels[count][1]), 16), int(hex(pixels[count][2]), 16))

		count += 1
im.show()
im.save("flag.png")

