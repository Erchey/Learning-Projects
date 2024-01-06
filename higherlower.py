from game_data import data
from art import higherlowerlogo, vs
import random
import os

# Clear the terminal screen based on the operating system
def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')

def output(data):
    random_dict = random.choice(data)
    name = random_dict['name']
    description = random_dict['description']
    country = random_dict['country']
    follower_count = random_dict['follower_count']
    return name, description, country, follower_count
# First data elements
first_data = output(data)
continue_game = True
score = 0


print(higherlowerlogo)



while continue_game:
    name1, description1, country1, follower_count1 = first_data
    print(f'Compare A: {name1}, a {description1}, from {country1}')
    print(vs)

    second_data = output(data)
    while second_data == first_data:
        second_data = output(data)
        
    name2, description2, country2, follower_count2 = second_data
    def CompareB(name=name2, description= description2, country=country2):
        print(f'Compare B: {name}, a {description}, from {country}')
    CompareB()
    
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_input == 'a' and second_data[3] > first_data[3]:
        print(f"Sorry that's wrong. Final Score: {score}.")
        continue_game = False
    elif user_input == 'b' and first_data[3] > second_data[3]:
        print(f"Sorry that's wrong. Final Score: {score}.")
        continue_game = False
    elif user_input not in ['a', 'b']:
        print(f"Invalid input. Final Score: {score}.")
        continue_game = False
    else:
        clear_screen()
        print(higherlowerlogo)
        score += 1
        print(f"You're Right! Current score: {score}")
    first_data = second_data






