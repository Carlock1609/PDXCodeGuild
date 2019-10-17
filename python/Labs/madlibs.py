#! python3

# v3 updated solution

import random

def get_adjective_list():
    adjective_list = []

    for i in range(3):
        adjective = input("Please enter in an adjectives: ")
        adjective_list.append(adjective)
    return adjective_list

def main():
    while True:
        game_on = input("Would you like to do a madlib?: (Yes or No)").lower()

        if game_on == "yes":
            get_adjectives = get_adjective_list()
            random.shuffle(get_adjectives)
            print(f"Jon is {get_adjectives[0]}. He is also {get_adjectives[1]} and even sometimes {get_adjectives[2]}.")
        else:
            print("Goodbye!")
            break

main()