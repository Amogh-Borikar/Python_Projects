import turtle
from turtle import Turtle, Screen
import random

my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title="Place your bet!", prompt="Which turtle will win the race?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_cor = [-70, -40, -10, 20, 50, 80]
turtles = []

for index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_cor[index])
    turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() >230:
            winning_turtle_color = turtle.pencolor()
            if winning_turtle_color == user_bet:
                print(f"You've won! {winning_turtle_color} color turtle won!")
            else:
                print(f"You've lost! {winning_turtle_color} color turtle won")
            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


my_screen.exitonclick()