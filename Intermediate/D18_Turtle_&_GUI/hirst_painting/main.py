import turtle as turtle_module
import random

turtle_module.colormode(255)
baby_blue = turtle_module.Turtle()

color_list = [(219, 254, 237), (84, 254, 155), (173, 146, 118), (254, 250, 254), (245, 39, 191), (158, 107, 56),
              (2, 1, 176), (151, 54, 251), (221, 254, 101), (253, 146, 193), (3, 87, 176), (249, 1, 246), (35, 34, 253),
              (1, 213, 212), (249, 0, 0), (254, 147, 146), (253, 71, 70), (244, 248, 254), (39, 249, 42),
              (85, 249, 253), (240, 1, 13), (5, 210, 216), (230, 126, 190), (2, 2, 107), (135, 152, 220),
              (174, 162, 249), (208, 118, 26), (253, 7, 4), (248, 6, 19)]

baby_blue.penup()
baby_blue.speed("fastest")
baby_blue.hideturtle()
baby_blue.setx(-300)
baby_blue.sety(-300)
baby_blue.setheading(0)


for i in range(10):
    for j in range(10):
        baby_blue.dot(20,random.choice(color_list))
        baby_blue.forward(50)
    baby_blue.setx(-300)
    baby_blue.sety((i * 50) - 250)

my_screen = turtle_module.Screen()
my_screen.exitonclick()

