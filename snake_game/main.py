from turtle import Screen
import time
from snake import Snake

sc = Screen()
sc.setup(height=600, width=600)
sc.bgcolor("black")
sc.title("SNAKE GAME")
sc.tracer(0)

# CREATES THE SNAKE
snake = Snake()

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

sc.exitonclick()
