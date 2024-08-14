from turtle import Turtle, Screen

tim = Turtle()

colors = ["red", "green", "blue", "yellow", "orange", "purple", "black", "cyan", "magenta", "wheat"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(colors[shape_side_n - 3])
    draw_shape(shape_side_n)
    
screen = Screen()
screen.exitonclick()
