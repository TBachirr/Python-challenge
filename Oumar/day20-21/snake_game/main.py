import time
import snake
import food
import scoreboard
from turtle import Screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

game_on = True
snak=snake.Snake()
foo =food.Food()
score = scoreboard.Scoreboard()

screen.listen()
screen.onkey(snak.up,"Up")
screen.onkey(snak.down,"Down")
screen.onkey(snak.left,"Left")
screen.onkey(snak.right,"Right")

while game_on:
    snak.move() 
    screen.update()
    time.sleep(0.1)
    
    if snak.head.distance(foo) < 15:
        foo.refresh()  
        snak.extend()
        score.increase_score()
        
    if snak.head.xcor() > 280 or snak.head.xcor() < -280 or snak.head.ycor() > 280 or snak.head.ycor() < -280:
        game_on = False
        score.game_over()
        
    for seg in snak.segment[1:]:
        if snak.head.distance(seg) < 10:
            game_on = False
            score.game_over()
        
screen.exitonclick() 
