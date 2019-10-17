#! python3

# v3 updated solution

def get_user_input():
    return int(input("Please enter in a number to convert it to a letter grade: "))

def get_grade(grade):
    if grade < 60:
        if grade % 10 < 4:
            grade = "-"
            print(f"You got a F{grade}")
        else:
            grade = "+"
            print(f"You got a F{grade}")
    elif grade >= 60 and grade < 70:
        if grade % 10 < 4:
            grade = "-"
            print(f"You got a D{grade}")
        else:
            grade = "+"
            print(f"You got a D{grade}")
    elif grade >= 70 and grade < 80:
        if grade % 10 < 4:
            grade = "-"
            print(f"You got a C{grade}")
        else:
            grade = "+"
            print(f"You got a C{grade}")
    elif grade >= 80 and grade < 90:
        if grade % 10 < 4:
            grade = "-"
            print(f"You got a B{grade}")
        else:
            grade = "+"
            print(f"You got a B{grade}")
    elif grade >= 90 and grade <= 100:
        if grade % 10 < 4:
            grade = "-"
            print(f"You got a A{grade}")
        else:
            grade = "+"
            print(f"You got a A{grade}")

def main():
    while True:
        get_grade(get_user_input())
        run_again = input("Do you want to convert your grade again?: (Yes or No)").lower()
        if run_again == "yes":
            continue
        else:
            print("Goodbye!")
            break
main()