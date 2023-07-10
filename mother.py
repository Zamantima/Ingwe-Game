from turtle import Turtle
FONT = ("Courier New", 24, "bold")

class Mother(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-80, 250)
        self.write("Othanda uMa", 24, font=FONT)

