import turtle as t
from random import choice, randint

bob = t.Turtle()
t.colormode(255)


def colors():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    p = (r, g, b)
    return p


directions = [0, 90, 180, 270]
sc = t.Screen().bgcolor("black")
bob.pensize(5)
bob.speed(0)

for i in range(900):
    bob.pencolor(colors())
    bob.fd(10)
    bob.setheading(choice(directions))

t.Screen().exitonclick()
