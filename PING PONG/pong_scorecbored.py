from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.score_update()

    def score_update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.l_score, align="center", font=("courier", 80, "normal"))

    def left_scored(self):
        self.l_score += 1
        self.score_update()

    def right_scored(self):
        self.r_score += 1
        self.score_update()
