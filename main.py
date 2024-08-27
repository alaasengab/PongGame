from turtle import Screen, Turtle
import time 
from paddel import Paddel
from ball import Ball
from scoreboard import score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# create Paddel 

r_paddel= Paddel((350,0))
l_paddel= Paddel((-350,0))
ball = Ball()
scoreboard= score()

# Listen function to keys to move up and down
screen.listen()
screen.onkey(r_paddel.go_up, "Up")
screen.onkey(r_paddel.go_down, "Down")

screen.onkey(l_paddel.go_up, "w")
screen.onkey(l_paddel.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()
    
    # Detect collision with wall 
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #Detect collision with r-paddel 
    if ball.distance(r_paddel) < 50 and ball.xcor() > 320 or ball.distance(l_paddel) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    if ball.xcor() > 380:  
        print("game over")
        ball.reset_position()
        scoreboard.l_point()
        
    if  ball.xcor() < -380: 
        print("game over")
        ball.reset_position()
        scoreboard.r_point()
        
     
        
screen.exitonclick()
