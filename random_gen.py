import turtle
turtle.penup()
turtle.hideturtle()
turtle.setx(-250)
turtle.sety(-250)
turtle.pendown()
turtle.tracer(20, 1)
w = turtle.pos()
s = turtle.heading()
turtle.seth(70)
eggy = []
def str_rep(a):
  y = ""
  for xs in a:
    if xs == "X":
      y += "F-[[X]+X]+F[+FX]-X[+XF]"
    elif xs == "F":
      y += "FF"
    else:
      y += xs
  return y

def iterate(a, t):
	for i in range(t):
		a = str_rep(a)
	return a

g = iterate("X",5)
for gs in g:
  if gs == "F":
    turtle.forward(3)
  elif gs == "-":
    turtle.left(25)
  elif gs == "+":
    turtle.right(25)
  elif gs == "[":
		eggy.append(turtle.heading())
		eggy.append(turtle.pos())
  elif gs == "]":
  	turtle.penup()
  	turtle.setpos(eggy.pop())
  	turtle.seth(eggy.pop())
  	turtle.pendown()
print(g)
turtle.exitonclick()
