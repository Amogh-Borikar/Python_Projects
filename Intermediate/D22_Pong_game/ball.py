from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")

    def move(self):
        self.penup()
        self.setheading(random.randint(0, 360))
        self.forward(20)
