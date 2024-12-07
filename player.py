import turtle
import math
from startwalls import StartWalls

images = [".\\paint\\volan_left_111.gif", ".\\paint\\volan_down_111.gif", ".\\paint\\volan_up_111.gif",
          ".\\paint\\snitch_111.gif",
          ".\\paint\\avadakedavra.gif", ".\\paint\\harry_fire_111.gif", ".\\paint\\volan_right_111.gif",
          ".\\paint\\harry_hat_111.gif",
          ".\\paint\\harry_right111.gif", ".\\paint\\harry_left111.gif", ".\\paint\\landscape (1).gif",
          ".\\paint\\happy_up111.gif", ".\\paint\\happy_down111.gif"]

for image in images:
    turtle.register_shape(image)


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape(".\\paint\\harry_right111.gif")
        self.penup()
        self.speed()
        self.fd(0)
        self.right = 1
        self.left = 0
        self.up = 0
        self.down = 0
        self.frame = 1

    def headright(self):

        if self.right == 1:
            pass

        if self.down == 1:
            self.rt(270)
            self.down = 0
            self.right = 1

        if self.left == 1:
            self.rt(180)
            self.left = 0
            self.right = 1

        if self.up == 1:
            self.rt(90)
            self.up = 0
            self.right = 1

    def headdown(self):

        if self.down == 1:
            pass

        if self.left == 1:
            self.rt(270)
            self.left = 0
            self.down = 1

        if self.up == 1:
            self.rt(180)
            self.up = 0
            self.down = 1

        if self.right == 1:
            self.rt(90)
            self.right = 0
            self.down = 1

    def headleft(self):

        if self.left == 1:
            pass

        if self.up == 1:
            self.rt(270)
            self.up = 0
            self.left = 1

        if self.right == 1:
            self.rt(180)
            self.right = 0
            self.left = 1

        if self.down == 1:
            self.rt(90)
            self.down = 0
            self.left = 1

    def headup(self):

        if self.up == 1:
            pass

        if self.right == 1:
            self.rt(270)
            self.right = 0
            self.up = 1

        if self.down == 1:
            self.rt(180)
            self.down = 0
            self.up = 1

        if self.left == 1:
            self.rt(90)
            self.left = 0
            self.up = 1

    def go_up(self):

        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24

        if self.frame == 0:
            self.shape(".\\paint\\happy_down111.gif")
            self.frame = 1
        else:
            self.shape(".\\paint\\happy_down111.gif")
            self.frame = 0

        if (move_to_x, move_to_y) not in StartWalls.walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24

        if self.frame == 0:
            self.shape(".\\paint\\happy_up111.gif")
            self.frame = 1
        else:
            self.shape(".\\paint\\happy_up111.gif")
            self.frame = 0

        if (move_to_x, move_to_y) not in StartWalls.walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()
        if self.frame == 0:
            self.shape(".\\paint\\harry_left111.gif")
            self.frame = 1
        else:
            self.shape(".\\paint\\harry_left111.gif")
            self.frame = 0

        if (move_to_x, move_to_y) not in StartWalls.walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()
        if self.frame == 0:
            self.shape(".\\paint\\harry_right111.gif")
            self.frame = 1
        else:
            self.shape(".\\paint\\harry_right111.gif")
            self.frame = 0

        if (move_to_x, move_to_y) not in StartWalls.walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 10:
            return True
        else:
            return False

    def destroy(self):
        self.goto(500, 500)
        self.hideturtle()
