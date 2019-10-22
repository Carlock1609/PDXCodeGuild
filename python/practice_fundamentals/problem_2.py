#! python3

def opposite(a,b):
    if a < 0 and b > 0:
        return True
    if a > 0 and b < 0:
        return True

print(opposite(2,-2))