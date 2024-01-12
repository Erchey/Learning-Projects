from turtle import *
import random



tim = Turtle()
forward_m = tim.forward
backward_m = tim.back
left_d = tim.left
right_d = tim.right
movement = [forward_m, backward_m]
direction = [left_d, right_d]
screen = Screen()

random_movement = 0

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()

    return(r, g, b)


while random_movement < 500:
    tim.speed(0)
    tim.color(random_color())
    tim.pensize(5)
    random.choice(direction)(90)
    random.choice(movement)(30)
    random_movement += 1
    
 
   


    
   
screen.exitonclick()
