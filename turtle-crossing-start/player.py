from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.pu()
        self.seth(90)
        self.goto(STARTING_POSITION)

    def up(self):
        self.fd(MOVE_DISTANCE)

    def down(self):
        self.bk(MOVE_DISTANCE)

