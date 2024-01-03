#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
random_number = random.randint(0, 2)
chosen_word = list(word_list[random_number])
length_of_word = len(chosen_word)
display = []
hangman = len(stages)

completed = False
for word in chosen_word:
    display.append('_')
while completed == False:
    guess = input(f'Guess a letter: {display}\n').lower()


    for position in range(length_of_word):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        hangman -= 1
        print(stages[hangman])
        
            
    if '_' not in display:
        print('You Win!')
        completed = True
    elif hangman == 0:
        completed = True
        print('You Lose')
            
print(display)
