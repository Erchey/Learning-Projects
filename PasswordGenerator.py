#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
total_nr_letters = nr_letters + nr_numbers + nr_symbols

letters_length = len(letters)
numbers_length = len(numbers)
symbols_length = len(symbols)



password = ''
 
for n in range(0, nr_letters):
    random_letters = random.randint(0, letters_length - 1)
    password += letters[random_letters]

for n in range(0, nr_numbers):
    random_numbers = random.randint(0, numbers_length - 1)
    password += numbers[random_numbers]

for n in range(0, nr_symbols):
    random_symbols = random.randint(0, symbols_length - 1)
    password += symbols[random_symbols]

char_list = list(password)
random.shuffle(char_list)

password = "".join(char_list)
print(password)




