#! python3

# 1 ft is 0.3048 m
# 1 mi is 1609.34 m
# 1 m is 1 m
# 1 km is 1000 m

# v1

def get_user_distance():
    return float((input("What is the distance in meters?: ")))

def get_user_units():
    get_units = input("What the units?: ")
    return get_units

def converter():
    m = 0
    units = get_user_units()

    if units == "ft":
        m = 0.3048
        return m
    elif units == "m":
        m = 1
        return m
    elif units == "mi":
        m = 1609.34
        return m
    elif units == "km":
        m = 1000
        return m

def display():
    return (get_user_distance() * converter())

print(display())
