#! python3

import random

def get_user_input():
    adjective_list = []

    for i in range(3):
        adjective = input("Please enter in an adjectives: ")
        adjective_list.append(adjective)

    return adjective_list

def get_random_adjective(adjective_list):
    return random.shuffle(adjective_list)

def display_lib(get_random_adjective, adjective_list):
    mad_lib = f"Jon is {adjective_list[0]}. He is also {adjective_list[1]} and even sometimes {adjective_list[2]}."


def madlib_game():
    adjective_list = []

    while True:
        game_on = input("Would you like to do a madlib?: (Yes or No)").lower()

        if game_on == "yes":
            get_adjectives = get_random_adjective(get_user_input())
            display_lib(get_adjectives, adjective_list)
        else:
            print("Goodbye!")
            break

madlib_game()
