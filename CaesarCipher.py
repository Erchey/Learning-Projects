from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def caesar(start_text, shift_amount, cipher_direction):

    end_text = ""
    if cipher_direction == 'decode':
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"Here's the {cipher_direction}d result: {end_text}")

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

        


# def encode():
#     encrypted_text = ''
#     for n in text:
#         for i in alphabet:
#             index = alphabet.index(i)
            
#             if i == n:
#                 index = (index + shift) % 26
#                 encrypted_text += alphabet[index]
#     print(f"Here's the encoded result: {encrypted_text}")

# def decode():
#     encrypted_text = ''
#     for n in text:
#         for i in alphabet:
#             index = alphabet.index(i)
            
#             if i == n:
#                 index = (index - shift) % 26
#                 encrypted_text += alphabet[index]
#     print(f"Here's the encoded result: {encrypted_text}")
# if direction == 'encode':
#     direction = encode()
# elif direction == 'decode':
#     direction = decode()
# else:
#     print('Enter a valid instruction!')



