from turtle import Screen, Turtle
tv=Turtle()
screen = Screen()
screen.listen()
def move_forward():
    tv.forward(10)
screen.onkey(key="space",fun=move_forward)
screen.exitonclick()