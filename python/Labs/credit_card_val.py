#! python3

# v1

# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.

# How do i split everything into different functions but i need the same digit list

def get_digit_list():
    digit_list = []
    for i in range(0,16):
        get_digits = input("Please enter in 16 digits: ")
        digit_list.append(get_digits)
    return digit_list

def get_check_digit(digit_list):
    check_digit = []
    check_digit.append(digit_list.pop(15))
    return check_digit, digit_list


def reverse_list(digit_list):
    

print(get_check_digit(get_digit_list()))