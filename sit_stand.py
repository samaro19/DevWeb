filein = open("Desktop/sitin.txt", "r")
fileout = open("Desktop/sitout.txt", "w")
use = filein.read().split()
ma = int(use[0]) * int(use[1])
if ma <= int(use[2]):
	print1 = int(use[2])-ma
	print2 = ma
	fileout.write(str(print2) + " " + str(print1))
else:
    fileout.write(use[2] + " " + "0")

