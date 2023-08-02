from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_point = 0
        self.r_point = 0
        self.create_scoreboard()

    def create_scoreboard(self):
        self.clear()
        self.setposition(-100, 200)
        self.write(self.l_point, align="center", font=("Arial", 50, "bold"))
        self.setposition(100, 200)
        self.write(self.r_point, align="center", font=("Arial", 50, "bold"))

    def point_l(self):
        self.l_point += 1
        self.create_scoreboard()

    def point_r(self):
        self.r_point += 1
        self.create_scoreboard()
