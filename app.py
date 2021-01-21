import random

magic_numbers = [random.randint(1, 10), random.randint(1, 10)]

user_number = 88

if user_number in magic_numbers:
    print("you got it right")

if user_number not in magic_numbers:
    print("You got it wrong")