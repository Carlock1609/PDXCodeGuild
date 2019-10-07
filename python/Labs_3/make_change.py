#! python3

# v2

def get_user_input():
    return float(input("Please enter in an amount of pennies to be converted to dollars: "))

def convert_pennies(change):
    return str(int(change * 100))

def display_game():
    get_change = get_user_input()
    print(f"{get_change} dollars converted to {convert_pennies(get_change)} pennies.")

display_game()
