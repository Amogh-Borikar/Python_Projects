# from turtle import Turtle, Screen
#
# baby_blue = Turtle()
#
# baby_blue.shape("turtle")
# baby_blue.shapesize(2)
# baby_blue.color("CornflowerBlue")
#
# baby_blue.forward(100)
#
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name",["Pikachu", "Charmander", "Squirtle"])
table.add_column("Type", ["electric", "fire", "water"])
table.align = "l"

print(table)