#! python3
# v1 :mans_shoe:
# LIST COMPREHENSIONS WERE THE ONLY THING THAT WORKED *** 

def get_digit_dict():
    credit_card_digits = [5,1,7,8,0,5,9,4,2,9,4,4,7,9,7,3]
    check_digit = credit_card_digits.pop(15)
    digit_dict = {"credit_card_digits": credit_card_digits, "check_digit": check_digit}
    return digit_dict

def reverse_digit_list(digit_dict):
    digit_dict["credit_card_digits"].reverse()
    return digit_dict

def get_double_digits(digit_dict):
    digit_dict["credit_card_digits"][::2] = [i*2 for i in digit_dict["credit_card_digits"][::2]]
    return digit_dict

def get_subtracted_digits(digit_dict):
    digit_dict["credit_card_digits"] = [i-9 if i > 9 else i for i in digit_dict["credit_card_digits"]]
    return digit_dict

def get_total_sum(digit_dict):
    add_total = sum(digit_dict["credit_card_digits"])
    final_digit = list(str(add_total))
    if int(final_digit[1]) == digit_dict["check_digit"]:
        print(f"The sum was {add_total} and the final digit was {final_digit[1]}.")
        return True
    else:
        print(f"The final digit {final_digit[1]} did not match the check digit")
        return False

def main():
    print(get_total_sum(get_subtracted_digits(get_double_digits(reverse_digit_list(get_digit_dict())))))
    
main()