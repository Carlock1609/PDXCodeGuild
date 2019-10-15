#! python3

# v1

# DIFFERENT SOLUTION!! WHY IS IT NOT WORKING

# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.

# How do i split everything into different functions but i need the same digit list

def main():
    credit_card_digits = [4,5,5,6,7,3,7,5,8,6,8,9,9,8,5,5]
    check_digit = []
    check_digit.append(credit_card_digits.pop(15))
    reversed_digits = credit_card_digits[::-1]
    doubled_list = []
    for i in reversed_digits[1::2]:
        doubled_list.append(i)
    for i in reversed_digits[::2]:
        i *= 2
        doubled_list.append(i)
    print(doubled_list)
        
# print(main())
credit_card_digits = [4,5,5,6,7,3,7,5,8,6,8,9,9,8,5,5]

list1 = [10,8,18,9,16,6,16,5,14,3,14,6,10,5,8]

list2 = [8,9,6,5,3,6,5,10,18,16,16,14,14,10,8]

reversed = credit_card_digits[::-1]
print(reversed)

print(list1 == list2)