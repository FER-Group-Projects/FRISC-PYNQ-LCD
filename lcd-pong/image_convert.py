from PIL import Image, ImageDraw
import sys

def frisc_hex(num):
	tmp = hex(num)[2:]
	if not tmp[0].isdigit():
		tmp = "0" + tmp
	return tmp

image = Image.open(sys.argv[1])
pixels = image.convert('RGB').load()
data = []
width, height = image.size
for y in range(height):
    for x in range(width):
        r,g,b = pixels[(x,y)]
        color = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
        data.append((color >> 8) & 0xFF)
        data.append(color & 0xFF)
print(",".join(frisc_hex(x) for x in data))
#print(len(data))