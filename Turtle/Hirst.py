import colorgram
import turtle
import random

# Extract colors from the image
colors = colorgram.extract('image.jpg', 30)
rgb_colors = [color.rgb for color in colors]

# Create a turtle
tim = turtle.Turtle()
tommy = turtle.Turtle()
tim.speed(0)

# Define movement and direction functions
movement = [tim.forward, tim.backward]
direction = [tim.left, tim.right]
screen = turtle.Screen()
# Set up the screen


#def pen_motion():
#tommy.forward(10)
tommy.color('pink')
tommy.penup()
tommy.goto(0, 15)
tommy.pendown()

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