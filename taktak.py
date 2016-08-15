filein = open("taktakin.txt", "r")
fileout = open("taktakout.txt", "w")
use = filein.read().split()
i = 2
use = int(use[0])
moons = 0
while i == 2:
  if (use-1)%11 == 0:
    fileout.write(str(moons) + " " + str(use))
    i = 1
  else:
    use = use * 2
    moons = moons + 1

a,b=0,int(open("taktakin.txt").read())
while b%11!=1:a,b=a+1,b*2
open("taktakout.txt","w").write("%d %d"%(a,b))
