from turtle import Turtle, Screen

tim = Turtle()
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'black', 'pink', 'brown', 'lime']
for i in range(4):
    for k in range(10):
        tim.color(colors[k])
        tim.pendown()
        tim.forward(10)
        tim.penup()
        tim.forward(10)
    tim.left(90)




screen = Screen()
screen.exitonclick()
