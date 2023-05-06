import turtle
import pandas as pd

guessed_state = []
screen = turtle.Screen()
screen.setup(width=725, height=491)
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

def get_mouse_click_co_or(x, y):
    print(x, y)


while len(guessed_state) <= 50:

    screen.title(f"{len(guessed_state)}/50 States covered")
    ans = screen.textinput(title="Guess the state", prompt="state the name ?")
    ans = ans[0].upper() + ans[1:]
    turtle.onscreenclick(get_mouse_click_co_or)

    if ans == "exit":
        break

    if ans in all_states:
        guessed_state.append(ans)
        t = turtle.Turtle()
        t.pu()
        t.hideturtle()
        state_data = data[data.state == ans]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(f'{ans}', align='center', font=('courier', 9, 'normal'))

screen.mainloop()
