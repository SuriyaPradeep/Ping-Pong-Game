from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def create_ball(self):
        self.shape('circle')
        self.color("white")
        self.penup()

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def bounce_x_r(self):
        self.x_move = -(abs(self.x_move))
        self.move_speed *= 0.9

    def bounce_x_l(self):
        self.x_move = (abs(self.x_move))
        self.move_speed *= 0.9

    def out_bounds(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()
