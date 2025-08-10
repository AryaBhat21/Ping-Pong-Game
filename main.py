from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()

scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # collision w top n bottom walls, change ball movement
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    # collision w r_paddle and l_paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320) :
        ball.bounce_x()

    # detect when R paddle misses
    if ball.xcor() > 380 :
        ball.reset_pos()
        scoreboard.l_point()

    if ball.xcor() < -382 :
        ball.reset_pos()
        scoreboard.r_point()


screen.exitonclick()