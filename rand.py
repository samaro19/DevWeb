from PIL import Image
import random
i = Image.new("RGB",(1000, 1000))
x = i.load()
d = 1

while d < 1000000:
	q = random.randint(1, 999)
	a = random.randint(1, 999)
	w = random.randint(5, 255)
	e = random.randint(5, 255)
	r = random.randint(5, 255)
	x[q, a] = (w, e, r)
	d += 1
i.show()
