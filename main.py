# US States game project
from score import Score
from state import State
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.screensize(700, 450)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

score = Score()
guesses = []

game_on = True
while game_on:
    answer_state = screen.textinput(title=f"{score.total}/50 States", prompt="Enter a State's name:").title()

    if answer_state in all_states and answer_state not in guesses:
        guesses.append(answer_state)
        score.increase_score()
        state_data = data[data.state == answer_state]
        place_state = State(state_data.state.item(), int(state_data.x), int(state_data.y))

    if len(guesses) >= 50:
        game_on = False

# All code before exit
screen.exitonclick()
