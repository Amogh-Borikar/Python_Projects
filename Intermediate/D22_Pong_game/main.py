from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("Pong")
my_screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

my_screen.listen()
my_screen.onkey(r_paddle.go_up, "Up")
my_screen.onkey(r_paddle.go_down, "Down")
my_screen.onkey(l_paddle.go_up, "w")
my_screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    ball.move()
    time.sleep(0.1)
    my_screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

my_screen.exitonclick()


