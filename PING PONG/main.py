from turtle import Screen
from paddle import Paddle

sc = Screen()

sc.setup(width=800, height=600)
sc.bgcolor("black")
sc.title("Ping-pong")
sc.tracer(0)
rp = Paddle(pos=(350, 0))
lp = Paddle(pos=(-350, 0))

sc.listen()
sc.onkeypress(rp.up, "Up")
sc.onkeypress(rp.down, "Down")
sc.onkeypress(lp.up, "w")
sc.onkeypress(lp.down, "s")



game_on = True
while game_on:
    sc.update()
sc.exitonclick()
