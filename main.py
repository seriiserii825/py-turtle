import random
import turtle as t

screen = t.Screen()
# screen.bgcolor("#242933")

t.colormode(255)
tim = t.Turtle()

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

def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def randomWalk():
    directions = [0, 90, 180, 270]
    tim.pensize(6)
    tim.speed(1)

    for _ in range(300):
        tim.color(randomColor())
        direction = random.choice(directions)
        tim.forward(20)
        tim.setheading(direction)

def drawACircle():
    tim.speed('fastest')
    gap = 1
    total_circles = int(360 / gap)
    for _ in range(total_circles):
        tim.color(randomColor())
        current_heading = tim.heading()
        tim.setheading(current_heading + gap)
        tim.circle(120)

# drawSquare()
# drawMultipleElementss()
# randomWalk()
drawACircle()

screen.exitonclick()
