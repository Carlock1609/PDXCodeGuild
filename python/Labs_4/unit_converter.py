#! python3

# 1 meter = 3.28084 in feet
# v1

def get_user_input():
    return float((input("Enter in number of feet to be converted to meters: ")))

def get_meters(feet):
    meters_to_feet = 0.3048
    return meters_to_feet * feet

print(get_meters(get_user_input()))
