import time
from turtle import Turtle, Screen


#CREATE 600X600 SCREEN
my_screen = Screen()

my_screen.setup(width=600, height=600)

my_screen.bgcolor("black")
my_screen.title("Snake Game")

#TURN OFF THE ANIMATION
my_screen.tracer(0)



#CREATE A SNAKE 1TURTLE = 20 WIDTH AND 20 HEIGHT
#X AND Y POSITION
start_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in start_positions:
    new_snake = Turtle('square')
    new_snake.color('white')
    new_snake.penup()
    new_snake.goto(position)
    segments.append(new_snake)



game_is_on = True

while game_is_on:
    my_screen.update()
    time.sleep(0.1)

#MOVE THE BODY AND MAKE THE BODY FOLLOW THE HEAD
    for segment_num in range(len(segments) - 1, 0, -1):
        new_x = segments[segment_num - 1].xcor()
        new_y = segments[segment_num - 1].ycor()
        segments[segment_num].goto(new_x, new_y)
    segments[0].forward(20)









my_screen.exitonclick()