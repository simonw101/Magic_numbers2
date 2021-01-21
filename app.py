import random

magic_numbers = [random.randint(0, 10), random.randint(0, 10)]

chances = 3

for i in range(chances):  # range(chances) is [0,1,2]

    print("This is attempt {}".format(i+1))

    user_number = int(input("Please pick a number between 0 and 9: "))

    if user_number in magic_numbers:
        print("you got it right")

    if user_number not in magic_numbers:
        print("You got it wrong")



