from turtle import Screen
from paddle import Paddle
from ball import Ball
from pong_scorecbored import Score
import time

sc = Screen()

sc.setup(width=800, height=600)
sc.bgcolor("black")
sc.title("Ping-pong")

sc.tracer(0)
rp = Paddle(pos=(350, 0))
lp = Paddle(pos=(-350, 0))
ball = Ball()
score = Score()

sc.listen()
sc.onkeypress(rp.up, "Up")
sc.onkeypress(rp.down, "Down")
sc.onkeypress(lp.up, "w")
sc.onkeypress(lp.down, "s")

game_on = True
while game_on:
    time.sleep(0.1)
    sc.update()
    ball.r_move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(rp) < 60 and ball.xcor() > 320 or ball.distance(lp) < 60 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.left_scored()

    if ball.xcor() < -380:
        ball.reset_position()
        score.right_scored()

sc.exitonclick()
