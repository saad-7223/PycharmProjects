from turtle import Turtle, Screen
from random import randint

race_is_on = False
sc = Screen()
sc.setup(width=500, height=400)
sc.bgcolor("black")
user_bet = sc.textinput(title="Turtle Race", prompt="which turtle will win the race \n(Red,Yellow,Blue,Green,Orange,"
                                                   "Purple,White)")

turtles = []
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white"]
y = -90
for i in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(-230, y)
    y += 30
    turtles.append(new_turtle)

if user_bet:
    race_is_on = True
while race_is_on:

    for j in turtles:
        if j.xcor() > 230:
            race_is_on = False
            winner = j.pencolor()
            if winner == user_bet:
                print(f"You have Won ! the {winner} turtle is the winner")
            else:
                print(f"You have Lost ! the {winner} turtle was the winner")
        distance = randint(0, 10)
        j.fd(distance)


sc.exitonclick()