line1 = ["⬜️", "⬜️", "⬜️"]
line2 = ["⬜️", "⬜️", "⬜️"]
line3 = ["⬜️", "⬜️", "⬜️"]
map = [line1, line2, line3]

print(f"{line1}\n{line2}\n{line3}")
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? (e.g., A1, B2, C3): ")

# Convert the input to row and column indices
letters = position[0].lower()
numbers = int(position[1]) - 1
abc = ['a', 'b', 'c'].index(letters)
map[numbers][abc] = 'X'
# Update the treasure map based on the user's input


# Print the updated treasure map
print(f"{line1}\n{line2}\n{line3}")
