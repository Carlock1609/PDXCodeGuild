#! python3

# Problem 1 Done**
# Given a the two lists below, combine them into a dictionary.
def combine(fruits,prices):
    return dict(zip(fruits,prices))
# print(combine(["apple", "banana", "pear"], [1.2,3.3,2.1]))

# Problem 2 Done**
# Using the result from the previous problem, iterate through the dictionary and calculate the average price of an item.
def average(combine):
    return (sum(combine.values())/3)
print(average({"apple":1.2,"banana":3.3,"pear":2.1}))

# Problem 3
# Average numbers whose keys start with the same letter. Output a dictionary containing those letters as keys and the averages.
def unify(d):
    pass
unify({'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6})