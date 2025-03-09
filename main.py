from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from midline import Mid_Line



screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

player_1 = Paddle((-350, 0))
player_2 = Paddle((350, 0))
ball = Ball()
line = Mid_Line()
line.mline()
Scoreboard = Scoreboard()

screen.listen()
screen.onkey(player_1.up, "w")
screen.onkey(player_1.down, "s")

screen.onkey(player_2.up, "Up")
screen.onkey(player_2.down, "Down")

is_game_on = True
while is_game_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    if ball.ycor() > 290 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 320 and ball.distance(player_2) < 50 or ball.xcor() < -320 and ball.distance(player_1) < 50:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.update()
        Scoreboard.lscore_1()

    if ball.xcor() < -380:
        ball.update()
        Scoreboard.rscore_2()


screen.exitonclick()
