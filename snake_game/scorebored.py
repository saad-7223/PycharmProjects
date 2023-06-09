from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 20, "normal")
with open("high_score.txt", mode="r") as file:
    H = file.read()

class Scorebored(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high = 0
        self.color("White")
        self.pu()
        self.goto(0, 270)
        self.write(f"Score : {self.score} Highscore :{H}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_scorebored(self):
        self.write(f"Score :{self.score} Highscore :{H}", align=ALIGNMENT, font=FONT)

    def scored(self):
        self.score += 1
        self.clear()
        self.Highscore()
        self.update_scorebored()

    def gameover(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)

    def Highscore(self):
        if self.score > int(H):
            with open("high_score.txt", mode="w") as f:
                f.write(f"{self.score}")
        else:
            with open("high_score.txt", mode="w") as f:
                f.write(f"{H}")
