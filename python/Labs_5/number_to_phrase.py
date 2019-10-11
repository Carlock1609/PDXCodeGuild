#! python3

# v1

def get_user_input():
    return int(input("Please enter in a number to be converted to phrase: (sixty-nine)"))

def get_tens(get_num):
    if get_num > 10:
        return get_num//10

def get_singles(get_num):
    if get_num > 10:
        return get_num%10

def convert_ten(get_tens):
    if get_tens >= 2 and get_tens < 3:
        return "Twenty"
    if get_tens >= 3 and get_tens < 4:
        return "Thrity"
    if get_tens >= 4 and get_tens < 5:
        return "Forty"
    if get_tens >= 5 and get_tens < 6:
        return "Fifty"
    if get_tens >= 6 and get_tens < 7:
        return "Sixty"
    if get_tens >= 7 and get_tens < 8:
        return "Seventy"
    if get_tens >= 8 and get_tens < 9:
        return "Eighty"
    if get_tens >= 9 and get_tens < 10:
        return "Ninety"

def convert_singles(get_singles):
    if get_singles == 0:
        return "Zero"
    if get_singles == 1:
        return "One"
    if get_singles == 2:
        return "Two"
    if get_singles == 3:
        return "Three"
    if get_singles == 4:
        return "Four"
    if get_singles == 5:
        return "Five"
    if get_singles == 6:
        return "Six"
    if get_singles == 7:
        return "Seven"
    if get_singles == 8:
        return "Eight"
    if get_singles == 9:
        return "Nine"

def main():
    tens = convert_ten(get_tens(get_user_input()))
    singles = convert_singles(get_singles(get_user_input()))

    print(f"{tens}-{singles}")

main()