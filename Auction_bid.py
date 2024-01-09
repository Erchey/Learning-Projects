import os

# Clear the terminal screen based on the operating system
def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Mac and Linux (here, 'posix' refers to Unix/Linux based systems)
    # else:
    #     _ = os.system('clear')

bids = {}
print('Welcome to the secret auction program.')
condition = True

def auction(bids):
    highest_price = 0
    highest_bidder = ''
    for people in bids:
        actual_bid = bids[people]
        if actual_bid > highest_price:
            highest_price = actual_bid
            highest_bidder = people
    print(f'The highest bidder is {highest_bidder} with ${highest_price}')
    

while condition == True:
    name =  input('What is your name?:\n')
    user_bid = int(input('What\'s your bid?: $\n'))
    other_players = input("Are there other bidders? Type 'yes' or 'no'\n").lower()
    bids[name] = user_bid

    if other_players == 'yes':
        clear_screen()
    elif other_players not in 'no':
        print('Invalid Input')
        other_players = input("Are there other bidders? Type 'yes' or 'no'\n").lower()
    else:
        condition = False
        auction(bids)
