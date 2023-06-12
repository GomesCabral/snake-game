from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color('white')
        self.goto(0, 270)
        self.update_score()

    def increase_scrore(self):
        self.score += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.write(f'Score: {self.score}', move=False, align='center', font=('Courier', 18, 'normal'))