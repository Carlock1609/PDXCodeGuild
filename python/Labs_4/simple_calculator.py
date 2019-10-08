#! python3

def get_first_number():
    return int(input("Please enter in a first num: "))

def get_operation():
    get_user_operation = input("Please enter in a operation: ")
    if get_user_operation == "-":
        get_user_operation = -
    elif get_user_operation == "+":
        get_user_operation == +
    elif get_user_operation == "*":
        get_user_operation == *

def get_second_nmber():
    return int(input("Please enter in a second num: "))

def display():
    first_num = get_first_number()
    operation = get_operation()
    second_num = get_second_number()

    return first_num + operation + second_num

print(display())
