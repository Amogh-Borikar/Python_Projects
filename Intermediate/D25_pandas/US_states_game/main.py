import turtle
import pandas as pd

screen = turtle.Screen()

screen.title("U.S. State Game")
image = "Intermediate/D25_pandas/US_states_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_data = pd.read_csv("Intermediate/D25_pandas/US_states_game/50_states.csv")
state_list = state_data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 guessed correct",
                                     prompt="Type the U.S. state name").title()

    if answer_state == "Exit":
        missing_states = [s for s in state_list if s not in guessed_states]
        # missing_states = []
        # for s in state_list:
        #     if s not in guessed_states:
        #         missing_states.append(s)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("Intermediate/D25_pandas/US_states_game/states_to_learn.csv")
        break
    if answer_state in state_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        current_state = state_data[state_data.state == answer_state]
        t.goto(int(current_state.x), int(current_state.y))
        t.write(answer_state)

screen.mainloop()