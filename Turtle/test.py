from turtle import *
import random

timmy_the_turtle = Turtle()
screen = Screen()
timmy_the_turtle.shape('turtle')
timmy_the_turtle.goto(0.00, -100)

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()

    return(r, g, b)

number_of_sides = 3

while number_of_sides <= 12:

    timmy_the_turtle.color(random_color())

    angle = 360 / number_of_sides
    for n in range(number_of_sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.left(angle)
    number_of_sides += 1

screen.exitonclick()
