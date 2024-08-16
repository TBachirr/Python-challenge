import turtle
t = turtle.Turtle()
screen = turtle.Screen()
t.speed("fastest")
def move_forward():
    t.forward(10)
def move_backward():
    t.backward(10)
def turn_left():
    t.left(10)
def turn_right():
    t.right(10)
def cleart():
    t.clear()
    t.penup()
    t.home()
    t.pendown()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="space", fun=cleart)

screen.exitonclick()