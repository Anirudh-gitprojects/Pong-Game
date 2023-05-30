from turtle import Turtle,Screen
from paddle import Paddle
from Ball import Balls
from scoreboard import Scoreboard
from player import Player
import time
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")



p1=Paddle((350,0))
p2=Paddle((-350,0))
ball=Balls()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(p2.go_up,"w")
screen.onkey(p2.go_down,"s")
screen.onkey(p1.go_up,"p")
screen.onkey(p1.go_down,"l")

first_name=input("Enter player 1 name: ")
second_name=input("Enter player 2 name: ")
player1=Player()
player1.add_player1(first_name)
player2=Player()
player2.add_player2(second_name)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.distance(p1) <50 and ball.xcor()>320 or ball.distance(p2)<50 and ball.xcor()<-320:
        ball.bounce_x()

    if ball.xcor()>380:
      ball.reset_position()
      scoreboard.l_point()

    if ball.xcor() <-380:
        ball.reset_position()
        scoreboard.r_point()




screen.exitonclick()















screen.exitonclick()