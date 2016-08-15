filein = open("countin.txt", "r")
fileout = open("countout.txt", "w")
use = filein.read().split()
use = int(use[0])
start = 1
while start <= use:
  fileout.write(str(start)+"\n")
  start = start + 1
