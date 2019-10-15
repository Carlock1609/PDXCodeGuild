#! python3

# v1

# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.

# How do i split everything into different functions but i need the same digit list

def get_credit_digits():
    credit_list = [4,5,5,6,7,3,7,5,8,6,8,9,9,8,5,5]
    return credit_list
    
def get_check_digit(credit_list):
    check_digit = []
    check_digit.append(credit_list.pop(15))
    return check_digit

def get_reverse_digits(credit_list):
    credit_list.pop(15)
    reversed_digits = credit_list[::-1]
    return reversed_digits
    
def get_double_digits(reversed_digits):
    for i in reversed_digits[0:15:2]:
       reversed_digits.append(i*2)
       reversed_digits.remove(i)
    return reversed_digits

def get_list_subtractions(reversed_digits):
    print(reversed_digits)
    for i in reversed_digits:
        if reversed_digits[i] > 9:
            reversed_digits[i] -= 9
    return reversed_digits

def main():
    reverse_nums = get_reverse_digits(get_credit_digits())
    double_digits = get_double_digits(reverse_nums)
    get_subtractions = get_list_subtractions(double_digits)

    print(get_subtractions)

print(get_double_digits(get_reverse_digits(get_credit_digits())))
# main()

list1 = [10,8,18,9,16,6,16,5,14,3,14,6,10,5,8]

list2 = [9,6,8,3,6,5,5,10,18,16,16,14,14,10,8]

list3 = [9,6,8,3,6,5,5,10,18,16,16,14,14,10,8]

print(list1 in list3)