from turtle import Turtle, Screen


#CREATE 600X600 SCREEN
my_screen = Screen()

my_screen.setup(width=600, height=600)

my_screen.bgcolor("black")
my_screen.title("Snake Game")



#CREATE A SNAKE 1TURTLE = 20 WIDTH AND 20 HEIGHT
#X AND Y POSITION
start_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in start_positions:
    new_snake = Turtle('square')
    new_snake.color('white')
    new_snake.goto(position)










my_screen.exitonclick()