from turtle import Turtle

class Paddle1(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def Up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)
    
    def Down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)

