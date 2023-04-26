from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def creating_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=3)
            new_car.color(random.choice(COLORS))
            new_car.pu()
            y_coordinates = random.randint(-270, 290)
            new_car.goto(x=270, y=y_coordinates)
            self.all_cars.append(new_car)

    def move_all_cars(self):
        for c in self.all_cars:
            c.backward(self.car_speed)

    def level_finish(self):
        self.car_speed += MOVE_INCREMENT
