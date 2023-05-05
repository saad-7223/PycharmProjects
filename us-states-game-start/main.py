import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("India States game")
screen.setup(width=800, height=970)
img = "india-outline-map.gif"
screen.addshape(img)
turtle.shape(img)

data = pd.read_csv("36_states.csv")
all_states = data.state.to_list()


def get_mouse_click_co_or(x, y):
    print(x, y)


ans = screen.textinput(title="Guess the state", prompt="state the name ?")
turtle.onscreenclick(get_mouse_click_co_or)

if ans in all_states:
    pass
screen.mainloop()