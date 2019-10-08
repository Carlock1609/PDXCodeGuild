#! python3

# v2

def average(nums_list):
    return nums_list / 5

def get_user_num():
    nums_list = []
    counter = int(input("Please enter how long you would like the number list: "))

    while len(nums_list) < counter:
        get_num = int(input("Please enter in a number: "))
        nums_list.append(get_num)
    return sum(nums_list)

def main():
    print("You will enter in a length of a list, aswell as the numbers. And then it will find the average of the list of numbers.")

    nums_list = get_user_num()

    print(average(nums_list))

main()
