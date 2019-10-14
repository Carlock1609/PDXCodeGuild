#! python3

# v2

def get_first_number():
    return int(input("Please enter in a first num: "))

def get_second_number():
    return int(input("Please enter in a second num: "))

def get_operation():
    get_user_operation = input("Please enter in a operation: ")

    if get_user_operation == "-":
        return get_first_number() - get_second_number()
    elif get_user_operation == "+":
        return get_first_number() + get_second_number()
    elif get_user_operation == "*":
        return get_first_number() * get_second_number()
    elif get_user_operation == "/":
        return get_first_number() / get_second_number()

def main():
    run_again = True

    while run_again:
        print(get_operation())

        play_again = input("Would you like to use calc again?: (Yes or No)").lower()

        if play_again == "yes":
            run_again = True
        else:
            print("Goodbye!")
            run_again = False

main()
