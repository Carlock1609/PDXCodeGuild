#! python3

def maximum_of_three(a,b,c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    if c >= a and c >= b:
        return c

print(maximum_of_three(4,2,3))