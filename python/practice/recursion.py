#! python3

# simple recursion examples

# Using recursion to count up from arbitrary number
def countUp(num):
    if num >= 1:
        countUp(num - 1)
        print(num)
# countUp(10)

from time import sleep
# Using recursion to coiuntdown from arbitrary number
def countDown(num):
    sleep(1)
    print(num)
    if num == 0:
        return True
    return countDown(num - 1)
# print("Blast off in t-minus...")
# message = "Blast off " if countDown(5) else ""
# print(message)

# Using a loop to calculate factorial
new_num = 1
num = 7
for i in range(1, num):
    new_num *= i 
# print(f"factorial calculated from loop : {new_num}")

# Using recursion to calculate factorial
def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)
# print(f"factorial calculated from recursion: {factorial(6)}")

def blastoff(num):
    if num > 0:
        print(num)
        blastoff(num-1)
    else:
        print(f'BlastOff!!!!')
# blastoff(3)

