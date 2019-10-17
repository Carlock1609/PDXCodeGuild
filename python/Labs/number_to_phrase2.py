#! python3

#2 

# different solution, try using dict() and also only one input 

def get_user_input():
    user_input = int(input("Please enter in a number to be turned into a phrase: (555 -> Five-Hundred and Fifty-Five)"))
    return user_input


def get_num_dict(user_input):
    hundreds_dict = {100: "One-Hundred",
                    200: "Two-Hundred",
                    300: "Three-Hundred",
                    400: "Four-Hundred",
                    500: "Five-Hundred",
                    600: "Six-Hundred",
                    700: "Seven-Hundred",
                    800: "Eight-Hundred",
                    900: "Nine-Hundred",}

    tens_dict = {10: "and Ten",
                20: "and Twenty",
                30: "and Thirty",
                40: "and Forty",
                50: "and Fifty",
                60: "and Sixty",
                70: "and Seventy",
                80: "and Eighty",
                90: "and Ninety",}

    singles_dict = {1: "-One",
                    2: "-Two",
                    3: "-Three",
                    4: "-Four",
                    5: "-Five",
                    6: "-Six",
                    7: "-Seven",
                    8: "-Eight",
                    9: "-Nine",}

    if user_input//100 in hundreds_dict:
        hundreds = hundreds_dict[user_input]
    if user_input%100 in tens_dict:
        tens = tens_dict[user_input]
    if user_input%10 in singles_dict:
        singles = singles_dict[user_input]
    print(f"{hundreds}{tens}{singles}")

def main():
    pass

# get_num_dict(get_user_input())

hundreds_dict = {100: "One-Hundred",
                200: "Two-Hundred",
                300: "Three-Hundred",
                400: "Four-Hundred",
                500: "Five-Hundred",
                600: "Six-Hundred",
                700: "Seven-Hundred",
                800: "Eight-Hundred",
                900: "Nine-Hundred",}

num = 500

if num//100 in hundreds_dict:
    hundreds = hundreds_dict[num]
print(hundreds)