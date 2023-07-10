import time
from turtle import Turtle, Screen
from ingwe import Ingwe
from children import Children
from scoreboard import ScoreBoard
from mother import Mother

Starting_pos_1 = (-250,0)
Starting_pos_2 = (250,0)

screen = Screen()
screen.title("Ingwe")
screen.bgcolor("brown")
ingwe_1 = Ingwe()
ingwe_2 = Ingwe()
mother = Mother()

screen.setup(width= 600, height=600)
screen.tracer(0)


player = Children()
score = ScoreBoard()
ingwe_1.create_ingwe(Starting_pos_1)
ingwe_2.create_ingwe(Starting_pos_2)

screen.listen()
screen.onkey(player.move_left_p1, "Left")
screen.onkey(player.move_right_p1, "Right")
screen.onkey(player.move_up_p1, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    ingwe_1.ingwe_move(player)
    ingwe_2.ingwe_move(player)
    score.update_board()

    if player.is_at_finish_line():
        player.go_to_start()
        ingwe_1.level_up()
        score.increase_level()

    if ingwe_1.distance(player) < 20:
        game_is_on = False
        score.game_over()

screen.exitonclick()