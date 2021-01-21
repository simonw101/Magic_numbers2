import random

magic_numbers = [random.randint(0, 9), random.randint(0, 9)]


def ask_user_and_check_number():
    user_number = int(input("Please pick a number between 0 and 9: "))

    if user_number in magic_numbers:
        return "you got it right"

    if user_number not in magic_numbers:
        return "You got it wrong"


def run_programme_x_times(num):
    for i in range(num):  # range(chances) is [0,1,2]

        print("This is attempt {}".format(i+1))

        message = ask_user_and_check_number()

        print(message)


user_attempts = int(input("How many times do you want to run program: "))
run_programme_x_times(user_attempts)
