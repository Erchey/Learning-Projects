student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
# new_dict = {key:value for (key, value) in student_dict.items()}
# print(new_dict)

import pandas
nato_alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')
student_data_frame = pandas.DataFrame(nato_alphabet)

#Loop through rows of a data frame
new_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}
user_input = input().upper()
diction = [new_dict[letter] for letter in user_input]
print(diction)

    #pass


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

