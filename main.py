from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# creating screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('PONG_GAME')
screen.tracer(0) #animation gets turn off

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


#screen listen function allows user to control paddle with computer keyboards
screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on: #updates animation which was turned offx
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #ball collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #right side paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #left side paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
#screen exitonclick makes screen not disappear automatically
screen.exitonclick()
