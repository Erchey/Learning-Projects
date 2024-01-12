###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram, turtle, random

tim = turtle.Turtle()
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)

forward_m = tim.forward
backward_m = tim.back
left_d = tim.left
right_d = tim.right
movement = [forward_m, backward_m]
direction = [left_d, right_d]
screen = turtle.Screen()

for color in colors:
    rgb_colors.append(color.rgb)
    r = int(color.rgb.r)
    g = int(color.rgb.g)
    b = int(color.rgb.b)
    screen.colormode(255)
    new_color = (r, g, b)
    tim.speed(1)
    tim.color(new_color)
    tim.pensize(5)
    random.choice(direction)(90)
    random.choice(movement)(30)

screen.exitonclick()