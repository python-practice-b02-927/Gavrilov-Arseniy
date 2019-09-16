import turtle
turtle.shape('turtle')
k=50
for i in range (10) :
	turtle.forward(k)
	turtle.right(90)
	turtle.forward(k)
	turtle.right(90)
	turtle.forward(k)
	turtle.right(90)
	turtle.forward(k)
	k+=10
	turtle.penup()
	turtle.forward(5)
	turtle.right(90)
	turtle.backward(5)
	turtle.pendown()

input()
