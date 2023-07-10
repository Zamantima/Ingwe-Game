from turtle import Turtle
STARTING_POSITION_P1 = (0, -250)
FINISH_LINE_Y = 200

class Children(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape("turtle")
        self.color("blue")
        self.penup()
        self.go_to_start()
        self.xmove = 10
        self.ymove = 10
        self.move_pace = 15

    def move_up_p1(self):
        self.setheading(90)
        self.forward(self.move_pace)

    def move_right_p1(self):
        self.setheading(360)
        self.forward(self.move_pace)

    def move_left_p1(self):
        self.setheading(180)
        self.forward(self.move_pace)

    def go_to_start(self):
        self.goto(STARTING_POSITION_P1)


    def is_at_finish_line(self):
        if self.ycor() > 200:
            return True
        else:
            return False
