import turtle
import math
import winsound
from walls import Walls
from start import StartPlayer
from startwalls import StartWalls


class Missile(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape(".\\paint\\avadakedavra.gif")
        self.speed = 4
        self.fd(10)
        self.penup()
        self.color("yellow")
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
            self.goto(StartPlayer.player.xcor(), StartPlayer.player.ycor())
            self.setheading(StartPlayer.player.heading())
            self.status = "firing"
            if Walls.lives != 3:
                winsound.PlaySound(".\\sound\\avada.wav", winsound.SND_ASYNC)

    def move(self):

        if self.status == "ready":
            self.goto(-2456, 3422)

        if self.status == "firing":
            self.fd(self.speed)

        if self.is_far(StartPlayer.player):
            self.setheading(StartPlayer.player.heading())
            self.status = "ready"

        if self.xcor() < -350 or self.xcor() > 300 or \
                self.ycor() < -350 or self.ycor() > 300:
            self.setheading(StartPlayer.player.heading())
            self.status = "ready"

        if (self.xcor(), self.ycor()) in StartWalls.walls:
            self.setheading(StartPlayer.player.heading())
            self.status = "ready"
