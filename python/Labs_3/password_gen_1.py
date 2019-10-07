#! python3

import string, random

def get_lower():
    # Lower loop
    pass_length_lower = (int(input("Please enter in how many lower_case letters you want: ")) - 1)

    lower_case_gen = string.ascii_lowercase
    lower_case = []
    lower_case_str = "".join(lower_case)

    while len(lower_case) <= pass_length_lower:
        rand_lower_letter = random.choice(lower_case_gen)
        lower_case.append(rand_lower_letter)
    return lower_case_str

def get_upper():
    # Upper loop
    pass_length_upper = (int(input("Please enter in how many upper_case letters you want: ")) - 1)

    upper_case_gen = string.ascii_uppercase
    upper_case = []
    upper_case_str = "".join(upper_case)

    while len(upper_case) <= pass_length_upper:
        rand_length_upper = random.choice(upper_case_gen)
        upper_case.append(rand_length_upper)
    return upper_case_str

def get_nums():
    # Nums loop
    pass_length_nums = (int(input("Please enter in how many numbers do you want: ")) - 1)

    number_list_gen = string.digits
    numbers_list = []
    numbers_list_str = "".join(numbers_list)

    while len(numbers_list) <= pass_length_nums:
        rand_length_nums = random.choice(number_list_gen)
        numbers_list.append(rand_length_nums)
    return numbers_list_str

def get_chars():
    # Special char loop
    pass_length_special = (int(input("Please enter in how many special characters do you want: ")) - 1)

    special_char_list = "!@#$%^&*"
    special_chars = []
    special_chars_str = "".join(special_chars)

    while len(special_chars) <= pass_length_special:
        rand_length_special = random.choice(special_char_list)
        special_chars.append(rand_length_special)
    return special_chars_str

def main(get_lower, get_upper, get_nums, get_chars):
    password = [lower_case_str, upper_case_str, numbers_list_str, special_chars_str]

    print("".join(password))

main(get_lower(), get_upper(), get_nums(), get_chars())
