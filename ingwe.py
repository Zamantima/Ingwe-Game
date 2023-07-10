from turtle import Turtle

class Ingwe(Turtle):
    def __init__(self):
        super().__init__()

    def create_ingwe(self, start_pos):
        self.shape("circle")
        self.penup()
        self.goto(start_pos)
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.forward(10)
        self.xmove = 10
        self.ymove = 10
        self.speed = 6

    def ingwe_move(self, child):
        self.setheading(self.towards(child))
        self.forward(self.speed)

    def level_up(self):
        self.speed += 2







