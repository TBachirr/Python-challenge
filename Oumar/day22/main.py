from paddle import Paddle
from ball import Ball
from scoarboard import Scoreboard
import time

scoreboard = Scoreboard()
paddle = Paddle((-350, 0))
paddle2 = Paddle((350, 0))
ball = Ball()

import turtle

# Configuration de la fenêtre
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # Arrête la mise à jour automatique de l'écran

# Création de la ligne centrale
divider = turtle.Turtle()
divider.color("white")
divider.penup()
divider.goto(0, -300)
divider.setheading(90)
divider.pensize(5)

# Trace la ligne centrale en plusieurs segments
for _ in range(15):
    divider.pendown()
    divider.forward(20)
    divider.penup()
    divider.forward(20)

divider.hideturtle()


wn.onkey(paddle.go_up, "Up")
wn.onkey(paddle.go_down, "Down")
wn.onkey(paddle2.go_up, "w")
wn.onkey(paddle2.go_down, "s")


wn.listen()

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    elif (ball.distance(paddle) < 50 and ball.xcor() < -320) or (
        ball.distance(paddle2) < 50 and ball.xcor() > 320
    ):
        ball.bounce_x()
    else:
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.R_point()
        if ball.xcor() < -380:
            scoreboard.L_point()
            ball.reset_position()
    wn.update()


wn.exitonclick()
