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
    if xs == "A":
      y += "+B-A-B+"
    elif xs == "B":
      y += "-A+B+A-"
    else:
      y += xs
  return y

def iterate(x, t):
	for i in range(t):
		x = str_rep(x)
	return x

g = iterate("A",10)
for gs in g:
  if gs == "A" or gs == "B":
    turtle.forward(0.5)
  elif gs == "+":
    turtle.left(60)
  elif gs == "-":
    turtle.right(60)
print(g)
turtle.exitonclick()
