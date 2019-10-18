#! python3

# v2 updated solution

def get_first_number():
    return int(input("Please enter in a first num: "))

def get_second_number():
    return int(input("Please enter in a second num: "))

def get_operation():
   operation = input("Please enter in an operation: ")

   operation_dict = {   "+": +,
                        "-": -,
                        "*": *,
                        "/": /, 
                    }
    print(operation_dict[operation])

def main():
    pass
get_operation()