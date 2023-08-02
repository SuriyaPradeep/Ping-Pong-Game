from turtle import Turtle

START_POS = [(350, 0), (-350, 0)]


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape("square")
        self.goto(position)
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)
