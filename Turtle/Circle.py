from turtle import Turtle, Screen
import random



tim = Turtle()
forward_m = tim.forward
backward_m = tim.back
left_d = tim.left
right_d = tim.right
movement = [forward_m, backward_m]
direction = [left_d, right_d]
screen = Screen()
circle = tim.circle



number_of_circles = 0

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()

    return(r, g, b)
space_size = 5
while number_of_circles < 360/space_size:
    tim.speed(0)
    tim.pensize(2)
    heading = tim.heading()
    tim.color(random_color())
    circle(100)
    tim.setheading(heading + space_size)
    number_of_circles+=1
    
    
    
   
screen.exitonclick()
