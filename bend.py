filein = open("bendin.txt", "r")
fileout = open("bendout.txt", "w")
use = filein.read().split()
recaone = (int(use[2])-int(use[0]))*(int(use[3])-int(use[1]))
recatwo = (int(use[6])-int(use[4]))*(int(use[7])-int(use[5]))
if use[3] < use[7] and use[2] < use[6]:
  recamid = (int(use[4])-int(use[2]))*(int(use[5])-int(use[3]))
  fileout.write(str(recaone+recatwo-recamid))
elif use[3] > use[7] and use[2] < use[6]:
  recamid = (int(use[5])-int(use[7]))-(int(use[3]-int(use[1]))*(int(use[6])-int(use[4]))-int(use[3])-int(use[1]))
  fileout.write(recaone+recatwo-recamid)
else:
  print("y")
