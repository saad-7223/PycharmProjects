from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.sc = 0
        self.score_update()

    def levelup(self):
        self.sc += 1
        self.score_update()

    def score_update(self):
        self.clear()
        self.pu()
        self.goto(-200, 230)
        self.hideturtle()
        self.color("black")
        self.write(f"Level : {self.sc}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
