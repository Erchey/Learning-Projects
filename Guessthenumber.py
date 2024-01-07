import random
from art import Guess_logo
print(Guess_logo)

lives = 0
number = random.randint(1, 100)
difficulty =  input("Choose a difficulty. Type 'hard' or 'easy': ")

if difficulty == 'hard':
    lives += 5
elif difficulty == 'easy':
    lives += 10
print(f'You have {lives} lives remaining!')

continue_game = False
def condition():
    while number != guess:
        if guess > number:
            print('Too High')
        else:
            print('Too Low')
        return


while not continue_game:
    lives -= 1
    guess =  int(input('I\'m thinking of a number from 1 - 100. Make a guess!\n'))
    if guess == number:
        print(f'You got it! The answer was {number}')
    else:
        print(f'Guess again. You have {lives} lives remaining.')
        condition()
    
    if lives == 0 and guess != number:
        print('Game Over. You Lost!')
        continue_game = True




 