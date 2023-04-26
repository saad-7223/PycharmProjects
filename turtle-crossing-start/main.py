import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
cars = []

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
score = Scoreboard()
screen.listen()
screen.onkeypress(player.up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.creating_car()
    car_manager.move_all_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False
        if player.reached_finish_line():
            player.go_to_start()
            car_manager.level_finish()
            score.levelup()

screen.exitonclick()