#! python3

# v2
# HOW DO I GET IT TO DO TENS!

def get_user_input():
    return int(input("Please enter in the same number twice to be converted into phrase: (55 -> Fifty-Five)"))

def get_hundreds(get_num):
    if get_num > 100:
        return get_num//100

def get_tens(get_num):
    if get_num > 100:
        return get_num//10

def get_singles(get_num):
    if get_num > 100:
        return get_num%100

def convert_hundreds(get_hundreds):
    list_hundreds = ["One-Hundred", "Two-Hundred", "Three-Hundred", "Four-Hundred", "Fifty-Hundred", "Sixty-Hundred", "Seven-Hundred", "Eight-Hundred", "Nine-Hundred"]

    if get_hundreds >= 1 and get_hundreds < 2:
        return list_hundreds[0]
    if get_hundreds >= 2 and get_hundreds < 3:
        return list_hundreds[1]
    if get_hundreds >= 3 and get_hundreds < 4:
        return list_hundreds[2]
    if get_hundreds >= 4 and get_hundreds < 5:
        return list_hundreds[3]
    if get_hundreds >= 5 and get_hundreds < 6:
        return list_hundreds[4]
    if get_hundreds >= 6 and get_hundreds < 7:
        return list_hundreds[5]
    if get_hundreds >= 7 and get_hundreds < 8:
        return list_hundreds[6]
    if get_hundreds >= 8 and get_hundreds < 9:
        return list_hundreds[7]
    if get_hundreds >= 9 and get_hundreds < 10:
        return list_hundreds[8]

def convert_tens(get_tens):
    

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
    tens = convert_hundreds(get_hundreds(get_user_input()))
    singles = convert_singles(get_singles(get_user_input()))
    
    print(f"{tens}-{singles}")


# WORKS
print(convert_hundreds(get_hundreds(get_user_input())))