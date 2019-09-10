import turtle
turtle.shape('turtle')
i=50
while i<160:
	turtle.forward(i)
	turtle.right(90)
	turtle.forward(i)
	turtle.right(90)
	turtle.forward(i)
	turtle.right(90)
	turtle.forward(i)
	i+=10
	turtle.penup()
	turtle.forward(5)
	turtle.right(90)
	turtle.backward(5)
	turtle.pendown()

input()
