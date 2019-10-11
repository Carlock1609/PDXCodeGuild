#! python3
# Rock paper scissors game

import random


def get_comp_turn():
    moves = ["Scissors", "Paper", "Rock"]
    return random.choice(moves)

def get_user_turn():
    moves = ["Scissors", "Paper", "Rock"]
    get_turn = input("Please enter in a move: (Rock, Paper or Scissors)").capitalize()
    while get_turn not in moves:
        get_user_turn()
    else:
        return get_turn


def determine_win(user, comp):
    if user == "Rock" and comp == "Scissors":
        print("You win!")
    elif user == "Scissors" and comp == "Paper":
        print("You win!")
    elif user == "Paper" and comp == "Rock":
        print("You win!")
    elif user == "Rock" and comp == "Paper":
        print("You lose!")
    elif user == "Paper" and comp == "Scissors":
        print("You lose!")
    elif user == "Scissors" and comp == "Rock":
        print("You lose!")

def main():
    print("Welcome to Rock Paper Scissors!")
    play_game = input("Do you want to play Rock Paper Scissors?: (Yes or No)").lower()
    
    if play_game == "yes":
        determine_win(get_user_turn(), get_comp_turn())
        print(f"The computer picked {get_comp_turn()}!")
    else:
        print("Goodbye!")
        
main()