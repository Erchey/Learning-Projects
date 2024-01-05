logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_/
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import random

card_array = {'A': 11, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'K': 10, 'Q': 10, 'J': 10}
def deal_card():
    return random.choice(list(card_array.values()))

user_card = []
computer_card = []

for card in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())

user_score = sum(user_card)
computer_score = sum(computer_card)
score = [user_score, computer_score]

def calculate_score():
    if len(user_card) == 2 and user_score == 21 or len(computer_card) == 2 and computer_score == 21:
        return 0
    continue_game = input("Do you want to draw another card? 'Yes' or 'No'\n").lower()
    if continue_game == 'yes':
        user_card.append(deal_card())

if computer_score < 17:
    computer_card.append(deal_card())
#conditions for winning
def conditions():
    if user_score > 21:
        return 'Bust! You Lose'
    elif computer_score > 21 and user_score <= 21:
        return 'You Win'
    elif computer_score == user_score:
        return 'Draw!'
    elif computer_score > user_score:
        return 'You Lose!'
    elif user_score > computer_score:
        return 'You win'
print(logo)
print(f"These are your cards {user_card}, and computer's {computer_card[0]}")
print(calculate_score())