import turtle
turtle.penup()
turtle.setx(-500)
turtle.sety(-300)
turtle.pendown()
turtle.hideturtle()
turtle.tracer(100, 1)
def str_rep(x):
  y = ""
  for xs in x:
    if xs == "F":
      y += "F+F-F-F+F"
    else:
      y += xs
  return y

def iterate(x, t):
	for i in range(t):
		x = str_rep(x)
	return x

g = iterate("F",7)
for gs in g:
  if gs == "F":
    turtle.forward(0.5)
  elif gs == "+":
    turtle.left(90)
  elif gs == "-":
    turtle.right(90)
print(g)
turtle.exitonclick()
