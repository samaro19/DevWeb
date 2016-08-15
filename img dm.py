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
for eggy in range (1, 31):
	for o in range(3, 999):
		for m in range(3, 999):
			q = random.random()
			if q <= 0.8:
				numb = random.randint(1, 8)
				if numb == 1:
					x[o, m] = x[o, m+1]
				elif numb == 2:
					x[o, m] = x[o+1, m+1]
				elif numb == 3:
					x[o, m] = x[o+1, m]
				elif numb == 4:
					x[o, m] = x[o+1, m-1]
				elif numb == 5:
					x[o, m] = x[o, m-1]
				elif numb == 6:
					x[o, m] = x[o-1, m-1]
				elif numb == 7:
					x[o, m] = x[o-1, m]
				elif numb == 8:
					x[o, m] = x[o-1, m+1]
				else:
					print("damn daniel")
i.show() 
		
