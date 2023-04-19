"""
this program uses the listening events in turtle as a function to make drawing
when the user presses some specific buttons !!!
"""

import turtle as t

bob = t.Turtle()
sc = t.Screen()
t.mode("standard")

def f():
    bob.fd(10)

def b():
    bob.bk(10)

def l():
    h = bob.heading() + 10
    bob.setheading(h)

def r():
    h = bob.heading() - 10
    bob.setheading(h)

def c():
    bob.penup()
    bob.clear()
    bob.home()
    bob.pendown()


sc.listen()
sc.onkeypress(f, "w")
sc.onkeypress(b, "s")
sc.onkeypress(r, "a")
sc.onkeypress(l, "d")
sc.onkeypress(c, "c")


t.exitonclick()
