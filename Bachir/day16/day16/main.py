# import turtle
# timmy = turtle.Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(400)
# myscreen = turtle.Screen()
# myscreen.exitonclick()
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
table.align = "l"
print(table)

