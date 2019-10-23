#! python3

# Problem 1 Done** 
# Get a string from the user, print out another string, doubling every letter.
def problem_1():
    user_input = "hello"
    [print(i*2, end="") for i in user_input]

# Problem 2 Done**
# Write a function that takes a string, and returns a list of strings, each missing a different character.
def problem_2(word):
    list1 = []
    for i in word:
        list1.append(word.replace(i, ""))
    print(list1)
# problem_2("kitten")

# Problem 3 Done**
# Return the letter that appears the latest in the english alphabet.
# IMPLEMENT .sort() METHOD PLEASE
def latest_letter(letters): 
    list1 = list(letters)
    list1.sort()
    return list1[-1]
# print(latest_letter("pneumonoultrazmicroscopicsilicovolcanoconiosixys"))

# Problem 4 Done**
# Write a function that returns the number of occurances of 'hi' in a given string.
def count_hi(word):
    return word.count("hi")
# print(count_hi("hihihi"))

# Problem 5 Done**
# Write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'
def cat_dog(word):
    dog_count = word.count("dog")
    cat_count = word.count("cat")
    return dog_count == cat_count     
# print(cat_dog("catdogcatdog"))

# Problem 6 Done**
# Return the number of letter occurances in a string.
def count_letter(letter, word):
    return word.count(letter)
# count_letter('i', 'antidisestablishmentterianism')
# count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')

# Problem 7 Done**
# Convert input strings to lowercase without any surrounding whitespace.
def lower_case(word):
    lower_word = word.lower()
    split_word = lower_word.split()
    return "".join(split_word)
# print(lower_case("SUPER!"))
# print(lower_case("        NANNANANANA BATMAN        "))