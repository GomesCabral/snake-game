import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


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

#Food
food = Food()

#Scoreboard
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    # MOVE THE BODY AND MAKE THE BODY FOLLOW THE HEAD
    snake.move()
    scoreboard

    #Collisin with food
    if snake.head.distance(food) < 17:
        food.refresh()
        snake.extend()
        scoreboard.increase_scrore()

    # Collisin with wall
    elif snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_is_on = False
        scoreboard.game_over()

    # Collisin with tail
    for segment in snake.segments:
        #BECAUSE THE FIRS SEGMENT IS THE SNAKE HEAD - IS AUTO GAME OVER
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()


my_screen.exitonclick()