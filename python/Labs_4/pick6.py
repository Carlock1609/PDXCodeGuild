#! python3

# v1

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

def num_matches(user_guesses,winning_nums):
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

def get_balance(winning_tickets_list):
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

def get_run_sim():
    sim_counter = 0
    sim_earnings = 0
    tickets_bought = 0

    while sim_counter < 1000:
        winning_nums = pick6()
        user_guesses = sim_user_guesses()
        total_tickets =  num_matches(user_guesses, winning_nums)
        run_sim = get_balance(total_tickets)
        print(f"You made {run_sim} on current ticket picks {user_guesses}, the winning tickets were {winning_nums}\n")
        sim_counter += 1
        sim_earnings += run_sim
        tickets_bought += 2
    roi = (sim_earnings - tickets_bought)/tickets_bought
    print(f"You have ${sim_earnings}.00")
    print(f"If it cost you $2 for every ticket lot, your ROI is {roi}")
    
def main():
   get_run_sim()
        

main()