import turtle
from turtle import Turtle, Screen
import random

baby_blue = Turtle()
turtle.colormode(255)

baby_blue.shape("turtle")
baby_blue.color("Blue")


# # Draw square
# for _ in range(4):
#     baby_blue.forward(100)
#     baby_blue.left(90)


# # draw dashed line
# for _ in range(15):
#     baby_blue.forward(10)
#     baby_blue.penup()
#     baby_blue.forward(10)
#     baby_blue.pendown()


# # draw shapes in order
# number_of_sides = 3
# for i in range(10):
#     baby_blue.color(random.random(), random.random(), random.random())
#     for _ in range(number_of_sides):
#         angle = 360 / number_of_sides
#         baby_blue.forward(100)
#         baby_blue.right(angle)
#     number_of_sides += 1


# # random walk
# baby_blue.pensize(10)
# baby_blue.speed(10)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
# for i in range (200):
#     baby_blue.color(color())
#     baby_blue.forward(30)
#     baby_blue.setheading(random.choice([0, 90, 180, 270]))


# Spirograph
baby_blue.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


current_heading = 0
for i in range(90):
    baby_blue.circle(100)
    current_heading += 4
    baby_blue.color(random_color())
    baby_blue.setheading(current_heading)

screen = Screen()
screen.exitonclick()
