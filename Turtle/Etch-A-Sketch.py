from turtle import Turtle, Screen
import random


screen =  Screen()
tim = Turtle()
forward_m = tim.forward
backward_m = tim.back
left_d = tim.left
right_d = tim.right

def move_forwards():
    forward_m(10)

def move_back():
    backward_m(10)

def move_anticlock():
    left_d(10)

def move_clock():
    right_d(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    
screen.listen()
screen.onkey(key='f', fun=move_forwards)
screen.onkey(key='s', fun=move_back)
screen.onkey(key='a', fun=move_anticlock)
screen.onkey(key='d', fun=move_clock)
screen.onkey(key='c', fun=clear)
screen.exitonclick()