from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")
tim.width(15)

colors = ["red", "green", "blue", "yellow", "orange", "purple", "black", "cyan", "magenta", "wheat"]

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice([0, 90, 180, 270]))
    
screen = Screen()
screen.exitonclick()