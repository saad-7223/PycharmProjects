import turtle as t
from random import choice

bob = t.Turtle()
colours = ["aquamarine", "medium orchid", "lawn green", "magenta", "orange red", "red"]
sc = t.Screen().bgcolor("black")

for i in range(3, 10):
    bob.color(choice(colours))
    dim = 360//i
    for j in range(i):
        bob.fd(50)
        bob.rt(dim)



