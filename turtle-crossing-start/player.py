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

    def reached_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True

    def go_to_start(self):
        self.goto(STARTING_POSITION)
