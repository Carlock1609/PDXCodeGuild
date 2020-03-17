#! python3

# Problem 1 Done**
# Write a function that tells whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)
def is_even(a):
    return a % 2 == 0
# is_even(2)

# Problem 2 Done**
# rite a function that takes two ints, a and b, and returns True if one is positive and the other is negative.
def opposite(a,b):
    if a < 0 and b > 0:
        return True
    if a > 0 and b < 0:
        return True
print(opposite(2,-2))

# Problem 3 Done**
# Write a function that returns True if a number within 10 of 100.
def near_100(num):
    return num >= 10 and num <= 100
# print(near_100(80))

# Problem 4 Done**
# Write a function that returns the maximum of 3 parameters.
def maximum_of_three(a,b,c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    if c >= a and c >= b:
        return c
# print(maximum_of_three(4,2,3))

# Problem 5 Done**
# Print out the powers of 2 from 2^0 to 2^20
def super_power(num):
    return [num**a for a in range(10)]
# print(super_power(2))