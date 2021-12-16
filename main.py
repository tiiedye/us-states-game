# US States game project
from turtle import Screen
import pandas

screen = Screen()
screen.title("US States Game")
screen.screensize(700, 450)
screen.bgpic("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")

# All code before exit
screen.exitonclick()
