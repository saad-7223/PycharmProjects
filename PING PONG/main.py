from turtle import Screen
from paddle import Paddle
from ball import Ball
from pong_scorecbored import Score
import time

sc = Screen()
sc.setup(width=800, height=600)
sc.bgcolor("black")
sc.title("Ping-pong")
sc.tracer(100)

# CREATING PADDLES
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
    time.sleep(ball.ball_speed)
    sc.update()
    ball.move()

    # DETECTION WITH WALL
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # DETECTION COLLISION WITH PADDLE
    if ball.distance(rp) < 50 and ball.xcor() > 320 or ball.distance(lp) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # DETECT R PADDLE MISSES
    if ball.xcor() > 380:
        ball.reset_position()
        score.left_scored()

    # DETECT L PADDLE MISSES
    if ball.xcor() < -380:
        ball.reset_position()
        score.right_scored()

sc.exitonclick()
