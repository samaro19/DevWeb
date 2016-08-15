k = 1
eggy = []
while k != 100000:
  N = len(str(k))
  Ktwo = str(int(k)*int(k))
  first = Ktwo[:N]
  second = Ktwo[N:]
  if second == "":
    second = int(0)
    last = int(first) + int(second)
  else:
    last = int(first) + int(second)
  if last == int(k):
    eggy.append(last)
  k = k + 1

print(eggy)
