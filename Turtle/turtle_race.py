from turtle import Turtle, Screen
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
position = [-100, -50, 0, 50, 100, 150]
screen =  Screen()
screen.setup(width=500, height=400)
is_on = True
turtles = []
user_guess = screen.textinput(title="Make your bet", prompt="")

for turtle in range(6):
    
    tim = Turtle('turtle')
    tim.penup()
    
    tim.goto(-230, position[turtle])
    tim.color(colors[turtle])
    turtles.append(tim)
    

while is_on:
    for turtle in turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)

        if turtle.xcor() > 230:
            computer_guess = turtle.pencolor()
            if user_guess == computer_guess:
                print('You Won')
            else:
                print(f'You Lost. The winner is {computer_guess}')
            is_on = False
            

screen.exitonclick()


