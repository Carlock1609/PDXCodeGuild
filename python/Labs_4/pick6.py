#! python3

# v2

import random

def pick6():
    winning_nums = []
    counter = 1

    while counter <= 6:
        gen_num = random.randint(1,1000)
        winning_nums.append(gen_num)
        counter += 1
    return winning_nums

def sim_user_guesses():
    guesses = []
    counter = 1

    while counter <= 6:
        gen_num = random.randint(1,1000)
        guesses.append(gen_num)
        counter += 1
    return guesses

def correct_nums(user_guesses,winning_nums):
    winning_tickets_list = 0

    if user_guesses[0] == winning_nums[0]:
        winning_tickets_list += 1
    if user_guesses[1] == winning_nums[1]:
        winning_tickets_list += 1
    if user_guesses[2] == winning_nums[2]:
        winning_tickets_list += 1
    if user_guesses[3] == winning_nums[3]:
        winning_tickets_list += 1
    if user_guesses[4] == winning_nums[4]:
        winning_tickets_list += 1
    if user_guesses[5] == winning_nums[5]:
        winning_tickets_list += 1
    return winning_tickets_list

def get_total_earnings(winning_tickets_list):
    total_earnings = 0

    if winning_tickets_list == 1:
        total_earnings += 4
    elif winning_tickets_list == 2:
        total_earnings += 7
    elif winning_tickets_list == 3:
        total_earnings += 100
    elif winning_tickets_list == 4:
        total_earnings += 50000
    elif winning_tickets_list == 5:
        total_earnings += 1000000
    elif winning_tickets_list == 6:
        total_earnings += 25000000
    return total_earnings

def main():
    sim_counter = 0
    sim_earnings = 0
    tickets_bought = 0
    sim_length = 1000

    while sim_counter < sim_length:
        total_tickets =  correct_nums(pick6(), sim_user_guesses())
        current_sim_earnings = get_total_earnings(total_tickets)
        print(f"You made {current_sim_earnings} on current ticket picks {sim_user_guesses()}, the winning tickets were {pick6()}\n")

        sim_counter += 1
        sim_earnings += current_sim_earnings
        tickets_bought += 2
    roi = (sim_earnings - tickets_bought)/tickets_bought
    print(f"You bought {sim_length} tickets, and made a total of ${sim_earnings}.00 ")
    print(f"It cost you $2 for every ticket lot, your ROI is {roi}")
    
main()