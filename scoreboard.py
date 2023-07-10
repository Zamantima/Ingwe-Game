from turtle import Turtle

FONT = ("Courier New", 14, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, -250)
        self.level = 1

    def update_board(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.update_board()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align="center", font=FONT)
