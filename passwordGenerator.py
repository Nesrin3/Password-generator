# Import modules
import random
import string


print("Welcome to the password generator!")
# Ask the user for input
total_number = int(input("Enter the total number of characters in the password: "))
letter_num = int(input("Enter the number of letters in password: "))
numbers_num = int(input("Enter the number of numbers in password: "))
symbols_num = int(input("Enter the number of symbols in password: "))

# Check if the total number of characters matches the sum of letters, numbers and symbols
if total_number == letter_num + numbers_num + symbols_num:
    # Generate a list of random letters(uppercase + lowercase)
    letters_random = random.choices(string.ascii_letters, k=letter_num)

    # Generate a list of random digits (0-9)
    numbers_random = random.choices(string.digits, k=numbers_num)

    # Generate a list of random symbols (e.g., é@#$%)
    symbols_random = random.choices(string.punctuation, k=symbols_num)

    # Combine all the random characters into a single list
    total_random = letters_random + numbers_random + symbols_random

    # shuffle the combined list to randomize the order
    random.shuffle(total_random)

    print("".join(total_random))
else:
    # If the input counts don't add up, notify the user
    print("Invalid input. The sum of letters, numbers and symbols doesn't match the password")
