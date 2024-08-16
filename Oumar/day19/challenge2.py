import turtle
import random
colors = ["red", "green", "blue", "orange", "purple"]
n=-150
is_race_on = False 
all_turtles = []
for turtle_index in range(0, 5):
    timmy = turtle.Turtle(shape="turtle")
    timmy.penup()
    timmy.color(colors[turtle_index])
    timmy.penup()
    timmy.goto(x=-230, y=n)
    all_turtles.append(timmy)
    n+=30
screen = turtle.Screen()
screen.setup(width=500, height=400)
user =screen.textinput(title="Turtle Race", prompt="Enter the colors of the turtles: ")

if user :
    is_race_on = True
while is_race_on:
    for t in all_turtles:
        if t.xcor() > 230:
            w_color = t.pencolor()
            is_race_on = False
            if user == w_color:
                print(f"You've won. The {w_color} turtle is the winner")
            else:
                print(f"You've lost. The {w_color} turtle is the winner")
        t.forward(random.randint(0,10))
        
    





# print(user)
screen.exitonclick()