import turtle as turtle

colors = ["blue", "black", "red", "yellow", "green"]
turtle.pensize(2)


def drawShape(size, color):
    turtle.pencolor(color)
    for i in range(8):
        turtle.forward(size)
        turtle.left(45)
    pass


for j in range(len(colors)):
    drawShape(50, colors[j])
    turtle.penup()
    turtle.forward(100 + 50)
    if j == 2:
        turtle.home()
        turtle.right(45)
        turtle.forward(110)
        turtle.left(45)

    turtle.pendown()

turtle.exitonclick()
