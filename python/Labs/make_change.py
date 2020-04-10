#! python3

# v2

# issue with pennies. Always one short

def main():
    get_user_input = float(input("Please enter in a float dollar amount to be converted to pennies: (150.05 or 4.50): "))

    quarters = (get_user_input//.25) 
    quarters_remainder = (get_user_input%.25)
    dimes = (quarters_remainder//.10)
    dimes_remainder = (quarters_remainder%.10)
    nickels = (dimes_remainder//.05)
    nickels_remainder = (dimes_remainder%.05)
    pennies = (nickels_remainder//.01)

    print(f"{quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies} pennies")

main()