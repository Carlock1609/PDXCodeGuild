#! python3

# v1

def get_user_input():
    return input("Please enter in a word to check whether it is a palindrome: ")

def check_palindrome(get_user_input):
    if get_user_input[::] == get_user_input[::-1]:
        return True
    
print(check_palindrome(get_user_input()))