from turtle import Turtle

ALIGNMENT = 'CENTER'
FONT = ('COURIER', 20, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def gameover(self):
        self.reset()
        self.color('white')
        self.write('Game Over😭', align=ALIGNMENT, font=FONT)
        

