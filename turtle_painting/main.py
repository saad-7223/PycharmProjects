import turtle as t
from random import choice
t.colormode(255)
list_of_color = [(229, 228, 226), (227, 223, 225), (199, 174, 117), (215, 225, 218), (224, 227, 233), (125, 37, 24), (163, 103, 56), (184, 158, 53), (6, 56, 82), (108, 68, 85), (46, 34, 32), (113, 160, 175), (23, 121, 170), (75, 37, 47), (66, 153, 135), (9, 66, 46), (87, 139, 59), (130, 39, 42), (182, 96, 80), (204, 202, 144), (144, 175, 158), (171, 151, 156), (178, 201, 185), (221, 181, 167), (31, 78, 61), (24, 76, 91), (88, 142, 156), (161, 108, 112), (213, 179, 182), (169, 199, 209)]
sc = t.Screen()
bob = t.Turtle()
bob.hideturtle()
bob.setheading(225)
bob.pu()
bob.fd(300)
bob.setheading(0)
for _ in range(10):
    for _ in range(10):
        bob.dot(20, choice(list_of_color))
        bob.pu()
        bob.fd(50)
    bob.setheading(90)
    bob.fd(50)
    bob.setheading(180)
    bob.fd(500)
    bob.setheading(0)

t.exitonclick()
