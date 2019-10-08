#! python3

# v1

import random

def get_random_num(get_guess):
    secret_num = random.randint(0,10)
    if get_guess == secret_num:
        return True

def get_user_guess():
    get_guess = int(input("Please enter in a number: "))
    return get_guess

def main():
    print("Welcome to guess a number!")
    print("You have 10 guesses to guess the secret number between 1-10.")
    guesses = 1

    while guesses <= 10:
        guess_eval = get_random_num(get_user_guess())

        if guess_eval != True:
            print("Wrong!")
            guesses += 1
        elif guesses == 10:
            print("You ran out of guesses!")
            break
        else:
            print(f"You guessed the correct number in {guesses} tries!")
            break

main()
