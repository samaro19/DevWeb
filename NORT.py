filein = open("manin.txt", "r")
fileout = open("manout.txt", "w")
use = filein.read().split()
r = int(use[0])
t = int(use[1])
if r%2 == 0 and t%2 == 0:
  fileout.write(str(int(r)*int(t)))
elif r%2 != 0 and t%2 != 0:
  fileout.write(str(int(r)*int(t)-1))
else: 
  fileout.write(str(r*t))
