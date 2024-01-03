# Write your code below this line 👇

# def prime_checker(number):
#     is_prime = True
    
#     for n in range(2, number):
#         if number % n == 0:
#             is_prime = False
    
#     if is_prime == False:
#         print(f'The number {number} is not a prime number!')
    
#     else:
#         print(f'The number {number} is a prime number!')

# Write your code above this line 👆
    
#Do NOT change any of the code below👇
# n = int(input('Enter a number to check if its a prime number!\n')) # Check this number
# prime_checker(number=n)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encode():
    

    if direction == 'encode':
        encode()
    
    else:
        print("Enter valid instruction")

