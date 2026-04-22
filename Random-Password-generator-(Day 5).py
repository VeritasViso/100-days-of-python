## Made by @VeritasViso on 22/04/2026 at 18:12pm.

# Random Password Generator (Day 5 of 100)

import random

print("Welcome to the PyPassword Generator!")

try:
    user_choice_letters = int(input("How many letters would you like in your password? "))
    ## letters part
    letters = "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    final_letters = []
    ## letters loop
    for i in range(user_choice_letters):
        random_number_letters = random.randint(0, 51)
        final_letters.append(letters[random_number_letters])

    ## symbols part
    symbols = "`", "£", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", "@", "#", "~", ",", "<", ".", ">", "/", "?"
    final_symbols = []

    user_choice_symbols = int(input("How many symbols would you like? "))
    ## symbols loop
    for i in range(user_choice_symbols):
        random_number_symbols = random.randint(0, 28)
        final_symbols.append(symbols[random_number_symbols])

    ## numbers part
    numbers = "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
    final_numbers = []

    user_choice_numbers = int(input("How many numbers would you like? "))
    ## numbers loop
    for i in range(user_choice_numbers):
        random_number_numbers = random.randint(0, 9)
        final_numbers.append(numbers[random_number_numbers])

    final_password = final_letters + final_symbols + final_numbers
    final_password_joined = ",".join(final_password)
    print(f"[{final_password_joined}]") # unshuffled list printed

    random.shuffle(final_password)
    joined_password_1 = ",".join(final_password)
    joined_password_2 = "".join(final_password)

    print(f"[{joined_password_1}]") # shuffled list printed
    print(f"Your password is: {joined_password_2}") # JOINED shuffled list printed.
except:
    print("You didn't type a number!")

# end of program
