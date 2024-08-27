from turtle import Screen, Turtle
import time 
from paddel import Paddel
from ball import Ball
from scoreboard import score
#--------------------------PongGame Description------------------------#
"""Pong is a classic arcade video game that involves two players controlling paddles on opposite sides of a screen, attempting to hit a ball back and forth. The objective is to score points by causing the ball to hit the opponent's paddle.

Here's a basic breakdown of the game mechanics:

Players: There are two players, each controlling a paddle.
Ball: A small, bouncing ball moves back and forth across the screen.
Scoring: When the ball hits a player's paddle, it bounces back. If the ball goes past a player's paddle without hitting it, the opposing player scores a point.
Game Over: The game ends when one player reaches a predetermined score limit.

"""
#--------------------------------------------------------------------------#

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
