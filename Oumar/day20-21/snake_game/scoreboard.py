import turtle
ALIGNEMENT = "center"
FONT = ("Arial", 20, "normal")
class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNEMENT, font=FONT)
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNEMENT, font=FONT)
        
