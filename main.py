from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(height=600, width=800)

screen.tracer(0)  # Restricting from showing the animation

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.listen()

is_game = True
i = 1
while is_game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x_r()

    # Detect collision with the l_paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x_l()

    # Detect Ball is out of bounds r_paddle
    if ball.xcor() > 380:
        ball.out_bounds()
        score.point_l()

    # Detect Ball is out of bounds l_paddle
    if ball.xcor() < -380:
        ball.out_bounds()
        score.point_r()

screen.exitonclick()
