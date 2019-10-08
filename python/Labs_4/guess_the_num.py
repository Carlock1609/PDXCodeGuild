#! python3

# v3

import random

def get_random_num():
    secret_num = random.randint(0,10)
    return secret_num

def get_user_guess():
    get_guess = int(input("Please enter in a number: "))
    return get_guess

def main():
    print("Welcome to guess a number!")
    print("You have 10 guesses to guess the secret number between 1-10.")
    guesses = 1
    random_num = get_random_num()


    while guesses <= 10:
        guess = get_user_guess()

        if guess != random_num:
            print("Wrong!")
            guesses += 1
            if guess > random_num:
                print("Too high!")
            elif guess < random_num:
                print("Too low!")
        elif guesses == 10:
            print("You ran out of guesses!")
            break
        else:
            print(f"Correct! You guessed the secret number in {guesses} tries!")
            break
main()
