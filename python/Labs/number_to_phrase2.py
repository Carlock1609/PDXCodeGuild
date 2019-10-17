#! python3

#2 

# different solution, try using dict() and also only one input 

# Problems: Figure out solution to print only Three-Hundred if user input 0
# Figure out if there is a cleaner way other than doing elif if statements

def get_user_input():
    user_input = int(input("Please enter in a number to be turned into a phrase: (555 -> Five-Hundred and Fifty-Five)"))
    return user_input

def get_num_tuple(user_input):
    hundreds_dict = {1: "One-Hundred",
                        2: "Two-Hundred",
                        3: "Three-Hundred",
                        4: "Four-Hundred",
                        5: "Five-Hundred",
                        6: "Six-Hundred",
                        7: "Seven-Hundred",
                        8: "Eight-Hundred",
                        9: "Nine-Hundred",
                        }

    tens_dict1 = {1: "and Ten",
                    2: "and Twenty",
                    3: "and Thirty",
                    4: "and Forty",
                    5: "and Fifty",
                    6: "and Sixty",
                    7: "and Seventy",
                    8: "and Eighty",
                    9: "and Ninety",
                    }

    tens_dict2 = {  0: "Ten",
                    1: "Eleven",
                    2: "Twelve",
                    3: "Thirteen",
                    4: "Fourteen",
                    5: "Fifteen",
                    6: "Sixteen",
                    7: "Seventeen",
                    8: "Eighteen",
                    9: "Nineteen",
                    }

    singles_dict = {1: " One",
                        2: "Two",
                        3: "Three",
                        4: "Four",
                        5: "Five",
                        6: "Six",
                        7: "Seven",
                        8: "Eight",
                        9: "Nine",
                        }
    
    if user_input%10 > 20:
        print(f"{hundreds_dict[user_input//100]}{tens_dict1[(user_input//10)%10]}{singles_dict[user_input%10]}")

    elif user_input%10 < 20 and user_input%10 > 10:
        print(f"{hundreds_dict[user_input//100]} and {tens_dict2[user_input%10]}")

    elif user_input%10 < 10:
        print(f"{hundreds_dict[user_input//100]} and {singles_dict[user_input%10]}")


def main():
    get_num_tuple(get_user_input())
main()