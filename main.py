import time
from turtle import Turtle, Screen
from snake import Snake


#CREATE 600X600 SCREEN
my_screen = Screen()

my_screen.setup(width=600, height=600)

my_screen.bgcolor("black")
my_screen.title("Snake Game")

#TURN OFF THE ANIMATION
my_screen.tracer(0)

#CREATE A SNAKE OBJECT
snake = Snake()

#CNTL DE SNAKE
my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    # MOVE THE BODY AND MAKE THE BODY FOLLOW THE HEAD
    snake.move()










my_screen.exitonclick()