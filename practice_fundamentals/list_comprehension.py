#! python3

# List comprehension notes

# i want a list of squares between 1 and 10
# def squares(num):
#     my_squares = []
#     for num in range(1, 11):
#         my_squares.append(num ** 2)
#     return my_squares
# print("from function:")
# print(squares(2))

# the easier way
# You dont need o declare the variable
# it returns without Var
# print("from list comp:")
# my_squares = [num ** 2 for num in range(1,11)]
# print(my_squares)

# names = ["David", "Helen", "Anne"]
# lower_names = [name.lower() for name in names]
# print(lower_names)

# print([number for number in range(0,21) if number % 2 == 0])

# LIST COMPREHENSION PRACTICE PROBLEMS******

# problem1
# def powertime(num):
#    return [num ** 2 for num in range(1,11)]
# print(powertime(2))

# problem2
# def even_nums(num):
#     return [num for num in range(1,21) if num % 2 == 0]
# print(even_nums(20))

# problem3
# old_dict = {"a": 1, "b": 2,}
# def swapskie(old_dict):
#     return [{value,key} for key, value in old_dict.items()]

# print(swapskie(old_dict))
# for key, value in old_dict.items():
#     print({value,key})

# problem4
# import string
# print(({char: ord(char) for char in string.ascii_lowercase}))
# dict1 = {}
# for char in string.ascii_lowercase:
#     dict1.update({char: ord(char)})
# print(dict1)