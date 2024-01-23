import turtle
from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.title('US States Game')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
data_list = data.state.to_list()
guessed_state = []


def get_mouse_click_coo(x, y):
    print(x, y)


while len(guessed_state) < 50:
    answer_state = turtle.textinput(title=f'{len(guessed_state)}/50 States Correct', prompt='Enter another state').title()
    if answer_state == 'Exit':
        missing_states = [state for state in data_list if state not in guessed_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break

    if answer_state in guessed_state:
        print('Already guessed')
    elif answer_state in data_list:
        guessed_state.append(answer_state)
        coordinate = data[data.state == answer_state]
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(coordinate.x), int(coordinate.y))
        t.write(f'{answer_state}', align='center', font=('Arial', 8, 'normal'))

turtle.onscreenclick(get_mouse_click_coo)
# turtle.mainloop()

