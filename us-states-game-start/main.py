import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("India States game")
screen.setup(width=770, height=550)
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pd.read_csv("36_states.csv")
all_states = data.state.to_list()

ans = screen.textinput(title="Guess the state", prompt="state the name ?")

print(all_states)