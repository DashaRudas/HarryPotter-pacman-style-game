import turtle

class Door(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape((".\\paint\\harry_fire_111.gif"))
        self.color("brown")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(1999, 1999)
        self.hideturtle()