from turtle import Turtle

ALIGNEMENT = "center"
FONT = ("bitmap", 80, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.r_score}", align=ALIGNEMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"{self.l_score}", align=ALIGNEMENT, font=FONT)

    def L_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def R_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNEMENT, font=FONT)
