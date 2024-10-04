import random
import turtle as t

class MyTurtle():
    def __init__(self):
        t.colormode(255)
        self.screen = t.Screen()
        self.screen.bgcolor('#242933')
        self.tim = t.Turtle()
        self.colors = ['#99201a', '#503696', 'green', 'purple', 'orange', 'black', 'pink', 'brown', 'magenta', 'lime']

    def drawShape(self, num_sides):
        angle = 360 / num_sides 
        for _ in range(num_sides):
            self.tim.forward(60)
            self.tim.left(angle)

    def drawMultipleElementss(self):
        for shape_side_n in range(3, 11):
            self.tim.color(self.randomColor())
            self.drawShape(shape_side_n)

    def drawSquare(self):
        for _ in range(4):
            for _ in range(10):
                self.tim.pendown()
                self.tim.speed(1)
                self.tim.forward(10)
                self.tim.penup()
                self.tim.speed(2)
                self.tim.forward(10)
            self.tim.left(90)

    def randomColor(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)

    def randomWalk(self):
        directions = [0, 90, 180, 270]
        self.tim.pensize(6)
        self.tim.speed(1)

        for _ in range(300):
            self.tim.color(self.randomColor())
            direction = random.choice(directions)
            self.tim.forward(20)
            self.tim.setheading(direction)

    def drawACircle(self, gap=10):
        self.tim.speed('fastest')
        total_circles = int(360 / gap)
        for _ in range(total_circles):
            self.tim.color(self.randomColor())
            current_heading = self.tim.heading()
            self.tim.setheading(current_heading + gap)
            self.tim.circle(80)

    def exitScreen(self):
            self.screen.exitonclick()
