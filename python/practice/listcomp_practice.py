#! python3

# Problem 1 Done**
# Write a comprehension to generate the first 10 powers of two.
def powers(nums):
    [print(i**2) for i in range(10)]
# powers(2)

# Problem 2 Done**
# Write a comprehension to generate the first 10 even numbers.
def evens(nums):
    [print(i) for i in range(10) if i % 2 == 0]
# evens([1,2,3,4,5,6,7,8,9,10])

# Problem 3 Done**
# Write a dictionary comprehension to swap keys and values of a given dictionary. So {'a': 1, 'b': 2} would become {1: 'a', 2: 'b'}.
def swapsky(dic):
    list1 = {value:key for key, value in dic.items()}
    return list1
# print(swapsky({"a":1,"b":2}))

import string
# Problem 4 Done**
# Write a dictionary comprehension to print each letter of the alphabet and its correstponding ASCII code (check out ord)
def letter_count():
    keys = []
    values = []

    [keys.append(i) for i in string.ascii_lowercase]
    [values.append(ord(i)) for i in string.ascii_lowercase]

    return dict(zip(keys,values))
# print(letter_count())