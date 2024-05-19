from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("Pong")
my_screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
draw_screen = Turtle()

draw_screen.hideturtle()
draw_screen.penup()
draw_screen.color("white")
draw_screen.goto(400, 300)
draw_screen.pendown()
draw_screen.goto(400, -300)
draw_screen.goto(-400, -300)
draw_screen.goto(-400, 300)
draw_screen.goto(400, 300)
draw_screen.penup()
draw_screen.goto(0, 300)
draw_screen.pendown()
draw_screen.goto(0, -300)

my_screen.listen()
my_screen.onkey(r_paddle.go_up, "Up")
my_screen.onkey(r_paddle.go_down, "Down")
my_screen.onkey(l_paddle.go_up, "w")
my_screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    ball.move()
    time.sleep(ball.move_speed)
    my_screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

my_screen.exitonclick()


