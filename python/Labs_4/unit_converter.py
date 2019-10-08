#! python3

# 1 ft is 0.3048 m
# 1 mi is 1609.34 m
# 1 m is 1 m
# 1 km is 1000 m

# v4

def get_user_distance():
    return float((input("What is the distance?: ")))

def get_user_input():
    get_input = input("What is the input?: ")
    return get_input

def get_user_output():
    get_output = input("What is the output?: ")
    return get_output

def converter():
    ft = 0
    m = 0
    mi = 0
    km = 0

    units_input = get_user_input()
    units_output = get_user_output()

    # feet to
    if units_input == "ft" and units_output == "m":
        ft = 0.3048
        return ft
    elif units_input == "ft" and units_output == "km":
        ft = 3280.84
        return ft
    elif units_input == "ft" and units_output == "mi":
        ft = 5280.0
        return ft

    # meters to
    if units_input == "m" and units_output == "ft":
        m = 3.28084
        return m
    elif units_input == "m" and units_output == "mi":
        m = 0.000621371
        return m
    elif units_input == "m" and units_output == "km":
        m = 0.001
        return m

    # miles to
    if units_input == "mi" and units_output == "ft":
        mi = 5280
        return mi
    elif units_input == "mi" and units_output == "m":
        mi = 1609.34
        return mi
    elif units_input == "mi" and units_output == "km":
        mi = 1.60934
        return mi

    # Kilometers to
    if units_input == "km" and units_output == "ft":
        km = 3280.84
        return km
    elif units_input == "km" and units_output == "m":
        km = 1000
        return km
    elif units_input == "km" and units_output == "mi":
        km = 0.621371
        return km

def display():
    return (get_user_distance() * converter())

print(display())
