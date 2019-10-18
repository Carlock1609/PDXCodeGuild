#! python3

# v2 updated solution

def get_first_number():
    return int(input("Please enter in a first num: "))

def get_second_number():
    return int(input("Please enter in a second num: "))

def get_operation():
   return input("Please enter in an opperation: ")

def main():
    while True:
        run_again = input("Do you want to enter in equation?: (yes or no)").lower()

        if run_again == "yes":
            print(eval(f"{get_first_number()} {get_operation()} {get_second_number()}"))
        else:
            print("Goodbye!")
            break

main()