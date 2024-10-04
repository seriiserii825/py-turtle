import random
from turtle import Turtle, Screen

tim = Turtle()

colors = ['#99201a', '#503696', 'green', 'purple', 'orange', 'black', 'pink', 'brown', 'magenta', 'lime']

def drawShape(num_sides):
  angle = 360 / num_sides 
  for _ in range(num_sides):
    tim.forward(100)
    tim.left(angle)

def drawMultipleElementss():
  for shape_side_n in range(3, 11):
    tim.color(colors[shape_side_n - 3])
    drawShape(shape_side_n)


def drawSquare():
    for _ in range(4):
        for _ in range(10):
            tim.pendown()
            tim.speed(1)
            tim.forward(10)
            tim.penup()
            tim.speed(2)
            tim.forward(10)
        tim.left(90)

def randomWalk():
    directions = [0, 90, 180, 270]
    tim.pensize(6)
    tim.speed(1)

    for _ in range(300):
        tim.color(random.choice(colors))
        direction = random.choice(directions)
        tim.forward(20)
        tim.setheading(direction)

# drawSquare()
# drawMultipleElementss()
randomWalk()

screen = Screen()
screen.bgcolor("#800080")
screen.exitonclick()
