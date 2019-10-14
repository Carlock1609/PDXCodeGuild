#! python3

# VERSION 1

# name = input("Please enter in a name: ")
# bodypart = input("Please enter in a bodypart: ")
# fluid = input("Please enter in a fluid: ")
# pill = input("Please enter in a pill: ")
#
# mad_lib = name + " is sick with the " + bodypart + " flu. Drink more " + fluid + " and take " + pill + " as needed."
#
# print(mad_lib)

# VERSION 2

# import random
#
# adjective_list = []
#
# for i in range(3):
#     adjective = input("Please enter in a three adjectives: ")
#     adjective_list.append(adjective)
#
# random.shuffle(adjective_list)
#
# mad_lib = "Jon is " + adjective_list[0] + ". He is also " + adjective_list[1] + " and even sometimes " + adjective_list[2] + "."
#
# print(mad_lib)

# VERSION 3

import random

adjective_list = []

while True:

    madlib_prompt = input("Would you like to do a madlib?: (Yes or No)")

    if madlib_prompt.lower() == "yes":
        for i in range(3):
            adjective = input("Please enter in an adjectives: ")
            adjective_list.append(adjective)

        random.shuffle(adjective_list)

        mad_lib = f"Jon is {adjective_list[0]}. He is also {adjective_list[1]} and even sometimes {adjective_list[2]}."
    else:
        print("Goodbye!")
        break

    print(mad_lib)
