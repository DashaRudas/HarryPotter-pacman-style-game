import turtle
import math
import winsound

class AvadaKedavra(turtle.Turtle):
    global player
    global lives
    global walls
    def __init__(self, startx, starty):
        turtle.Turtle.__init__(self)
        self.shape(".\\paint\\avadakedavra.gif")
        self.speed = 4
        self.fd(10)
        self.penup()
        self.color("yellowgreen")
        self.status = "ready"
        self.goto(-1000, 1000)

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 20:
            return True
        else:
            return False

    def is_far(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance > 100:
            return True
        else:
            return False

    def fire(self):
        if self.status == "ready":
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"
            if lives != 3:
                winsound.PlaySound("avada.wav", winsound.SND_ASYNC)

    def move(self):
        global player
        if self.status == "ready":
            self.goto(-2456, 3422)

        if self.status == "firing":
            self.fd(self.speed)

        if AvadaKedavra.is_far(player):
            self.setheading(player.heading())
            self.status = "ready"

        if self.xcor() < -350 or self.xcor() > 300 or \
                self.ycor() < -350 or self.ycor() > 300:
            self.setheading(player.heading())
            self.status = "ready"

        if (self.xcor(), self.ycor()) in walls:
            self.setheading(player.heading())
            self.status = "ready"
