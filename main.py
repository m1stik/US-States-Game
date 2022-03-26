import pandas
import turtle
import os
from drawMap import DrawMap

dir = os.path.dirname(os.path.abspath(__file__))

screen = turtle.Screen()
screen.title("U.S States Game")
image = r"\blank_states_img.gif"
screen.addshape(dir + image)
turtle.shape(dir + image)

drawMap = DrawMap()

correct_guesses = []

csv = r"\50_states.csv"
states_data = pandas.read_csv(dir + csv)
states_dict = states_data["state"].to_dict()

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States correct", prompt="What's another state's name?").title()

    for item in states_dict:
        if states_dict[item] == answer_state and answer_state not in correct_guesses:
            state_index = states_data[states_data['state'] == answer_state].index.item()
            state_x = states_data.at[state_index, "x"]
            state_y = states_data.at[state_index, "y"]
            drawMap.display_state(answer_state, state_x, state_y)
            correct_guesses.append(answer_state)
            break
        else:
            pass
    
    if len(correct_guesses) == 50:
        drawMap.gameover()
        game_is_on = False

turtle.mainloop()