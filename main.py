from turtle import Screen
from Paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

POS = [(320, 0), (-320, 0)]

# Create the Screen
screen = Screen()
screen.setup(700, 500)
screen.bgcolor("black")
screen.title("PONG (The Famous Arcade Game)")
screen.tracer(0)
screen.listen()

# Creating the paddles
r_paddle = Paddle()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
r_paddle.goto(POS[0])

l_paddle = Paddle()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
l_paddle.goto(POS[1])

ball = Ball()

scoreboard = ScoreBoard()

speed = ["slow", "normal", "fast", "fastest"]

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 220 or ball.ycor() < -220:
        ball.y_bounce()

    # Detect collision with paddle
    if ball.xcor() > 290 and ball.distance(r_paddle) < 60 or ball.xcor() < -290 and ball.distance(l_paddle) < 60:
        ball.x_bounce()

    if ball.xcor() > 330:
        ball.reset_pos()
        time.sleep(2)
        scoreboard.l_point()

    if ball.xcor() < -330:
        ball.reset_pos()
        time.sleep(2)
        scoreboard.r_point()







































screen.exitonclick()
