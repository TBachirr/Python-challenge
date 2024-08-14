import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list =[(243, 242, 239), (99, 6, 51), (172, 158, 33), (75, 94, 172), (232, 209, 73), (10, 35, 127), (212, 91, 34), (177, 104, 155), (104, 122, 210), (25, 95, 40), (243, 237, 240), (33, 103, 48), (112, 130, 212), (233, 236, 245), (183, 115, 161)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
    
screen = turtle_module.Screen()
screen.exitonclick()