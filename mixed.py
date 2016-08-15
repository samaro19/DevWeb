filein = open("mixin.txt", "r")
fileout = open("mixout.txt", "w")
use = filein.read().split()
if int(use[0])%int(use[1]) == 0:
    fileout.write(str(int(use[0])/int(use[1])))
else:
    rem = int(use[0])%int(use[1])
    mix = int(use[0])-rem
    fileout.write(str(int(mix/6)) + " " + str(rem) + "/" + str(use[1]))
