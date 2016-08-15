import turtle
turtle.penup()
turtle.sety(00)
turtle.pendown()
turtle.hideturtle()
turtle.tracer(20, 1)
def str_rep(x):
  y = ""
  for xs in x:
    if xs == "A":
      y += "BF+AFA+FB-"
    elif xs == "B":
      y += "AF-BFB-FA+"
    else:
      y += xs
  return y

def iterate(x, t):
	for i in range(t):
		x = str_rep(x)
	return x

g = iterate("A",10)
for gs in g:
  if gs == "F":
    turtle.forward(1)
  elif gs == "-":
    turtle.left(90)
  elif gs == "+":
    turtle.right(90)
print(g)
turtle.exitonclick()
