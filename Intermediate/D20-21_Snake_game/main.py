from turtle import Turtle, Screen


screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game!")
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    segment_1 = Turtle(shape="square")
    segment_1.color("white")
    segment_1.goto(position)

screen.exitonclick()