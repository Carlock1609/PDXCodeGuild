#! python3

import string

# def add(a, b):
#     return a + b
# print(add(2,2))


# Problem 1
# Get a string from the user, print out another string, doubling every letter.
def problem_1():
    user_input = "hello"
    [print(i*2, end="") for i in user_input]

# Problem 2
# Write a function that takes a string, and returns a list of strings, each missing a different character.
def problem_2(word):
    for i in word:
        if i in word:
            pass
# problem_2("kitten")

# Problem 3
# Return the letter that appears the latest in the english alphabet.
def latest_letter(letters):
    letter_list = string.ascii_lowercase
    for i in letters:
        if letters[i] > letters: 
            print(letter_list)
# latest_letter("pneumonoultramicroscopicsilicovolcanoconiosis")

# Problem 4
# Write a function that returns the number of occurances of 'hi' in a given string.
def count_hi(word):
    counter = 0
    if word.find("hi"):
        counter += 1
    print(counter)
count_hi("hihi")

# Problem 5
# Write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'


# Problem 6
# Return the number of letter occurances in a string.


# Problem 7
# Convert input strings to lowercase without any surrounding whitespace.
