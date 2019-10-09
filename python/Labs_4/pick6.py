#! python3

import random

def pick6():
    winning_nums = []
    counter = 1

    while counter <= 5:
        gen_num = random.randint(1,100)
        winning_nums.append(gen_num)
        counter += 1
    return winning_nums

def get_user_guesses():
    guesses = []
    counter = 1

    while counter <= 5:
        get_guesses = int(input("Please enter in 6 numbers: (1-100)"))
        guesses.append(get_guesses)
        counter += 1
    return guesses
