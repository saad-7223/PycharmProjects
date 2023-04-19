import turtle as t
from random import randint

bob = t.Turtle()
t.colormode(255)
sc = t.Screen().bgcolor("black")

def colors():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    p = (r, g, b)
    return p


def draw_spiro(off_size):
    for i in range(int(360 / off_size)):
        bob.pencolor(colors())
        bob.circle(50)
        curr = bob.heading()
        bob.setheading(curr + off_size)


draw_spiro(5)
bob.speed("fastest")
t.Screen().exitonclick()
