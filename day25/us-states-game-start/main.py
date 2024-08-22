import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image) 
gessing_states = []
while len(gessing_states) < 50:
    user_answer = screen.textinput(title=f"{len(gessing_states)}/50 Guessed ", prompt="What's another state's name?").title()
    data = pd.read_csv("50_states.csv")
    all_states = data.state.tolist()
    if user_answer in all_states: 
        t = turtle.Turtle(shape="turtle")
        t.penup()
        t.hideturtle()
        x = data[data.state == user_answer].x
        y = data[data.state == user_answer].y
        t.goto(float(x), float(y))
        t.write(user_answer)
        gessing_states.append(user_answer)
    elif user_answer == "Exit":
        missing_states = [state for state in all_states if state not in gessing_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
