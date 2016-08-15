import turtle
turtle.penup()
turtle.sety(200)
turtle.setx(400)
turtle.pendown()
turtle.hideturtle()
turtle.tracer(5000, 1)
def str_rep(x):
  y = ""
  for xs in x:
    if xs == "X":
      y += "X+YF+"
    elif xs == "Y":
      y += "-FX-Y"
    else:
      y += xs
  return y

def iterate(x, t):
	for i in range(t):
		x = str_rep(x)
	return x

g = iterate("FX",19)
for gs in g:
  if gs == "F":
    turtle.forward(1)
  elif gs == "-":
    turtle.left(90)
  elif gs == "+":
    turtle.right(90)
print(g)
turtle.exitonclick()
