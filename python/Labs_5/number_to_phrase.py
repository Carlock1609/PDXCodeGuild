#! python3

# v2
# HOW DO I GET IT TO DO TENS

def get_user_input():
    return int(input("Please enter in the same number twice to be converted into phrase: (55 -> Fifty-Five)"))

def get_tens(get_num):
    if get_num > 10:
        return get_num//10

def get_singles(get_num):
    if get_num > 10:
        return get_num%10

def convert_ten(get_tens):
    list_tens = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    if get_tens >= 2 and get_tens < 3:
        return list_tens[0]
    if get_tens >= 3 and get_tens < 4:
        return list_tens[1]
    if get_tens >= 4 and get_tens < 5:
        return list_tens[2]
    if get_tens >= 5 and get_tens < 6:
        return list_tens[3]
    if get_tens >= 6 and get_tens < 7:
        return list_tens[4]
    if get_tens >= 7 and get_tens < 8:
        return list_tens[5]
    if get_tens >= 8 and get_tens < 9:
        return list_tens[6]
    if get_tens >= 9 and get_tens < 10:
        return list_tens[7]

def convert_singles(get_singles):
    list_singles = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

    if get_singles == 0:
        return list_singles[0]
    if get_singles == 1:
        return list_singles[1]
    if get_singles == 2:
        return list_singles[2]
    if get_singles == 3:
        return list_singles[3]
    if get_singles == 4:
        return list_singles[4]
    if get_singles == 5:
        return list_singles[5]
    if get_singles == 6:
        return list_singles[6]
    if get_singles == 7:
        return list_singles[7]
    if get_singles == 8:
        return list_singles[8]
    if get_singles == 9:
        return list_singles[9]

def main():
    tens = convert_ten(get_tens(get_user_input()))
    singles = convert_singles(get_singles(get_user_input()))
    
    print(f"{tens}-{singles}")

main()