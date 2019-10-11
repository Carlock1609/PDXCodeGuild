#! python3

# v2

def get_user_input():
    return int(input("Please enter in a dollar amount to be converted to pennies: (150 or 4.50)"))

def convert_pennies(change):
    return str(int(change * 100))

def main():
    get_change = get_user_input()
    print(f"{get_change}.00 dollars converted to pennies is {convert_pennies(get_change)} pennies.")

main()()
