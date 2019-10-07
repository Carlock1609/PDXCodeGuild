#! python3

def get_user_input():
    return int(input("Please enter in an amount of pennies to be converted to dollars: "))

def nearest_dollar(change):
    return str(change / 100)

def display_game():
    get_change = get_user_input()
    print(f"{get_change} pennies converted to ${nearest_dollar(get_change)} dollars.")

display_game()
