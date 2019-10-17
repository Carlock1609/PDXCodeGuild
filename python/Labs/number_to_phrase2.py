#! python3

#2 

# different solution, try using dict() and also only one input 

# Dictionary in a dictionary?

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


# get_num_dict(get_user_input())

def main():
    pass


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



print(hundreds_dict[num1 // 10])