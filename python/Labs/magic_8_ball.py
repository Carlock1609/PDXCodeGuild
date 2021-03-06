#! python3

# v1

import random

def gen_response_list():
    list = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no",
    "Outlook not so good", "Very doubtful"]
    return list

def get_rand_response():
    return random.choice(gen_response_list())

def main():
    print("Welcome to Magic Eight Ball Game!")

    while True:
        play_again = input("Would you like to play?: ").lower()

        if play_again == "yes":
            player_input = input("Please enter in a question: ")
            print(f"{get_rand_response()}\n ")
        else:
            print("Goodbye!")
            break

main()
