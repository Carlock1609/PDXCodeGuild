#! python3

# v2 updated solution

def get_equation():
    return input("Please enter in a number, an operation and another number with spaces imbetween: example(5 + 4) ")

def main():
    while True:
        run_again = input("Do you want to enter in equation?: (yes or no) ").lower()

        if run_again == "yes":
            print(eval(f"{get_equation()}"))
        else:
            print("Goodbye!")
            break

main()