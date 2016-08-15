eggy = [0]
Y = eggy[-1] + 1
eggy.append(Y)
while eggy[-1] <= 1000000:
    Y = eggy[-1] + eggy[-2]
    eggy.append(Y)
print(eggy)
