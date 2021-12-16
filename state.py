from turtle import Turtle

FONT = ("Arial", 8, "normal")


class State(Turtle):
    def __init__(self, state, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(f"{state}", font=FONT)

