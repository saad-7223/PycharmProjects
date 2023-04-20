import random
from turtle import Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 260)
        self.goto(x, y)

