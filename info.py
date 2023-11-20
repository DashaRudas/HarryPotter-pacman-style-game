import turtle


class Info:
    def __init__(self):
        self.gold = 0
        self.lives = 3
        self.pen = turtle.Turtle()

    def draw_border(self):
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-324, 324)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(645)
            self.pen.rt(90)
            self.pen.fd(665)
            self.pen.rt(90)

        self.pen.penup()
        self.pen.ht()
        self.pen.pendown()

    def show_gold(self):
        self.pen.undo()
        msg = "Деньги: %s" % self.gold
        self.pen.penup()
        self.pen.goto(-324, 334)
        self.pen.write(msg, font=("Arial", 16, "normal"))

    def show_rules(self):
        msg = "W,A,S,D - заклятия, стрелочки - передвижение"
        self.pen.penup()
        self.pen.goto(-324, -380)
        self.pen.write(msg, font=("Arial", 16, "normal"))
        self.pen.pendown()
        self.pen.penup()
        self.pen.ht()

    def win(self):
        msg = (""" 
            Распределяющая шляпа укажет путь в Хогвартс! Вы победили!
                      Нажмите (x) чтобы выйти

               """)
        self.pen.penup()
        self.pen.goto(-250, 304)
        self.pen.write(msg, font=("Arial", 16, "normal"))

    def dead(self):
        msg = (""" 
                          Вы проиграли(   
                    Нажмите (x) чтобы выйти

               """)
        self.pen.penup()
        self.pen.goto(-250, 304)
        self.pen.write(msg, font=("Arial", 16, "normal"))

    def show_lives(self):
        self.pen.undo()
        msg = "Жизни:%s" % self.lives
        self.pen.penup()
        self.pen.ht()
        self.pen.goto(250, -380)
        self.pen.color("white")
        self.pen.write(msg, font=("Arial", 16, "normal"))
