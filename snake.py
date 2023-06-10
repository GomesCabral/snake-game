from turtle import Turtle


#X AND Y POSITION
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

MOVE_DISTANCE = 20

#DIRECTIONS
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

     # CREATE A SNAKE 1TURTLE = 20 WIDTH AND 20 HEIGHT
    def create_snake(self):
        for position in START_POSITIONS:
            new_snake = Turtle('square')
            new_snake.color('white')
            new_snake.penup()
            new_snake.goto(position)
            self.segments.append(new_snake)

    # MOVE THE BODY AND MAKE THE BODY FOLLOW THE HEAD
    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)