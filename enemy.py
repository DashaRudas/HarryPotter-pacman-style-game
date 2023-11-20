import turtle
import math
import random
from startwalls import StartWalls
from start import StartPlayer


class Enemy(turtle.Turtle):

    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape(".\\paint\\volan_left_111.gif")
        self.penup()
        self.exp = 5
        self.speed(0)
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])
        self.frame = 0
        self.frame = ""

    def is_close(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 100:
            return True
        else:
            return False

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
            self.shape(".\\paint\\volan_up_111.gif")

        elif self.direction == "down":
            dx = 0
            dy = -24
            self.shape(".\\paint\\volan_down_111.gif")

        elif self.direction == "left":
            dx = -24
            dy = 0
            self.shape(".\\paint\\volan_left_111.gif")

        elif self.direction == "right":
            dx = 24
            dy = 0
            self.shape(".\\paint\\volan_right_111.gif")

        else:
            dx = 0
            dy = 0

        if self.is_close(StartPlayer.player):
            if StartPlayer.player.xcor() < self.xcor():
                self.direction = "left"

            elif StartPlayer.player.xcor() > self.xcor():
                self.direction = "right"

            elif StartPlayer.player.ycor() < self.ycor():
                self.direction = "down"

            elif StartPlayer.player.ycor() > self.ycor():
                self.direction = "up"

        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        if (move_to_x, move_to_y) not in StartWalls.walls:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction = random.choice(["up", "down", "left", "right"])

        turtle.ontimer(self.move, t=random.randint(100, 300))

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()
