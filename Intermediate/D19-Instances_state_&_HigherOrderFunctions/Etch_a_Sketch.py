from turtle import Turtle, Screen

baby_blue = Turtle()
my_screen = Screen()


def forward():
    baby_blue.forward(10)


def backward():
    baby_blue.backward(10)


def left():
    new_heading = baby_blue.heading() + 10
    baby_blue.setheading(new_heading)

def right():
    new_heading = baby_blue.heading() - 10
    baby_blue.setheading(new_heading)

def clear():
    baby_blue.home()
    baby_blue.clear()

my_screen.listen()
my_screen.onkey(forward, "w")
my_screen.onkey(backward, "s")
my_screen.onkey(left, "a")
my_screen.onkey(right, "d")
my_screen.onkey(clear, "c")
my_screen.exitonclick()
