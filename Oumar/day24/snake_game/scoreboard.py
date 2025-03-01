import turtle
ALIGNEMENT = "center"
FONT = ("Arial", 20, "normal")
class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        with open("myfile.txt") as data:
            self.high_score = int(data.read())
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNEMENT, font=FONT)
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=ALIGNEMENT, font=FONT)
    def reset(self):
        if self.score > self.high_score :
            self.high_score = self.score
            with open("myfile.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard
            