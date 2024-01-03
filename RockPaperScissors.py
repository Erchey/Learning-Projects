import random

print('Rock, Paper, Scissors!')
user_input = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

RPS = ['Rock', 'Paper', 'Scissors']

computer_guess = random.randint(0, 2)
print(RPS[user_input])

print('Computer chose:')
print(RPS[computer_guess])


if user_input == 0 and computer_guess == 2:
    print('You Win!')
elif user_input == 1 and computer_guess == 0:
    print('You Win!')
elif user_input == 2 and computer_guess == 1:
    print('You Win!')
elif user_input == computer_guess:
    print('It\'s a tie')
else:
    print('You Lose!')
