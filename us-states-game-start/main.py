import turtle

screen = turtle.Screen()
screen.title("India States game")
screen.setup(width=770, height=550)
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

ans = screen.textinput(title="Guess the state", prompt="state the name ?")

