#! python3

# v2

# What happened to palindrome?
# redo palindrome

def get_user_input():
    get_input = input("Please enter in a word to check whether it is an anagram: ").lower()
    return get_input

def remove_spaces(get_input1, get_input2):
    replace1 = get_input1.replace(" ", "")
    replace2 = get_input2.replace(" ", "")
    sort1 = sorted(replace1)
    sort2 = sorted(replace2)
    return sort1, sort2

def check_anagram():
    check_anagram = (remove_spaces(get_user_input(),get_user_input()))
    if check_anagram[0] == check_anagram[1]:
        return True

def main():
    print(check_anagram())

main()
