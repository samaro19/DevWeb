import turtle
import random
BIGDIST = 100
SMALLDIST = 50
turtle.speed(0) # Fastest
turtle.hideturtle() # Only show the turtle's trail.
turtle.colormode(255)
turtle.pensize(5)
turtle.sety(10)
turtle.setx(10)
turtle.tracer(2, 1)
count = 0
i = 0
r = 1
g = 1
b = 1
while True:
	i += 1
	x = random.randint(1,3)
  	turtle.forward(random.randint(1, 100))
  	if x == 1:
		turtle.left(90)
	else:
		turtle.right(90)
	turtle.color(r, g, b)
	r = random.randint(1,255)
	g = random.randint(1,255)
	b = random.randint(1,255)
	if i%100 == 0:
		turtle.penup()
		turtle.sety(10)
		turtle.setx(10)
		turtle.pendown()
turtle.exitonclick()
