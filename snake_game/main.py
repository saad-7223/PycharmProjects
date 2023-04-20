from turtle import Screen
import time
from snake import Snake
from food import Food
from scorebored import Scorebored

sc = Screen()
sc.setup(height=600, width=600)
sc.bgcolor("black")
sc.title("SNAKE GAME")
sc.tracer(0)

# CREATES THE SNAKE
snake = Snake()
food = Food()
score = Scorebored()

sc.listen()
sc.onkeypress(snake.up, "Up")
sc.onkeypress(snake.down, "Down")
sc.onkeypress(snake.left, "Left")
sc.onkeypress(snake.right, "Right")

game_on = True

while game_on:
    sc.update()
    time.sleep(0.1)
    # MOVES THE SNAKE
    snake.move()
    # COLLISION DETECTION
    if snake.head.distance(food) < 15:
        food.refresh()
        score.scored()
        snake.extend()

    # WALL COLLISION
    # building a reference line
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.gameover()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.gameover()
sc.exitonclick()
