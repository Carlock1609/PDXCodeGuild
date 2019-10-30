#! python3

# Problem 1 Done**
# Write a function using random.randint to generate an index, use that index to pick a random element of a list and return it.
import random
def random_element():
    list1 = ["apples", "bananas", "pears"]
    return list1[random.randint(0,(len(list1)-1))]
# print(random_element())

# Problem 2 Done**
# Write a REPL which asks users for a list of numbers, which they enter, until they say 'done'. Then print out the list.
def get_list():
    list1 = []
    while True:
        user_input = input("Enter a number or type 'done':" ).lower()
        if user_input != "done":
            list1.append(int(user_input))
        else:
            print((list1))
            break
# get_list()

# Problem 3 Done**
# Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.
def eveneven(list):
    counter = 0
    for i in list:
        if i % 2 == 0:
            counter += 1
    if counter % 2 == 0:
        return True
    else:
        return False
# print(eveneven([5,6,2]))
# print(eveneven([5,5,2]))

# Problem 4 Done**
# Print out every other element of a list, first using a while loop, then using a for loop.
def print_every_other(nums):
    counter = 0
    while counter < (len(nums)/2):
        for i in nums[::2]:
            counter += 1
            print(i)      
# print_every_other([0,1,2,3,4,5,6,7,8,])

# Problem 5 Done**
# Write a function that returns the reverse of a list.
def reverse(nums):
    nums.reverse()
    return nums
# print(reverse([1,2,3]))

# Problem 6 Done**
# Write a function to move all the elements of a list with value less than 10 to a new list and return it.
def extract_less_than_ten(nums):
    new_list = []
    [new_list.append(i) for i in nums if i < 10]
    return new_list
# print(extract_less_than_ten([1,2,3,10,20,14,16,8,6]))

# Problem 7 Done**
# Write a function to find all common elements between two lists.
def common_elements(nums1, nums2):
    commons = []
    [commons.append(ele) for ele in nums1 if ele in nums2]
    return commons
# print(common_elements([1,2,3],[2,3,6]))

# Problem 8 Done**
# Write a function to combine two lists of equal length into one, alternating elements.
def combine(nums1,nums2):
    new_list = []
    while len(new_list) <= 5:
            new_list.append(nums1.pop(0))
            new_list.append(nums2.pop(0))
    return new_list
# print(combine(["a","b","c"],[1,2,3]))

# Problem 9
# Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number
def find_pair(nums,target):
    for i in nums:
        print(i)
        if i + nums[0] == target:
            print(f"{i}")
# find_pair([5,6,2,3], 7)

# Problem 10
# Write a function that merges two lists into a single list, where each element of the output list is a list containing two elements, one from each of the input lists.
def merge(nums1,nums2):
    list1 = []
    list2 = []
    list3 = []
    new_list = [list1, list2, list3]

    while True:
        list1.append(nums1.pop(0))
        list1.append(nums2.pop(0))
        list2.append(nums1.pop(0))
        list2.append(nums2.pop(0))
        list3.append(nums1.pop(0))
        list3.append(nums2.pop(0))
        break
    return new_list
# print(merge([5,2,1],[6,8,2]))

# Problem 11
# Write a function combine_all that takes a list of lists, and returns a list containing each element from each of the lists.


# Problem 12
# Write a function that takes n as a parameter, and returns a list containing the first n Fibonacci Numbers.


# Problem 13
# Write functions to find the minimum, maximum, mean, and (optionally) mode of a list of numbers.


# Problem 14
# Write a function which takes a list as a parameter and returns a new list with any duplicates removed.