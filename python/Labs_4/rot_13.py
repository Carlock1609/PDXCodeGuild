#! python3
# v1

import string

def get_abc_list():
    abc_list = list("abcdefghijklmnopqrstuvwxyz ")
    return abc_list

def get_rot_list():
    rot_list = list("nopqrstuvwxyzabcdefghijklmd ")
    return rot_list

def get_user_input():
    return input("Please enter in a letter to be encrypted: ")

def main():
    rot_list = get_rot_list()
    abc_list = get_abc_list()
    encrypt_list = []

    print("Welcome to rot 13!\nEnter in one letter at a time to be encrypted.")

    get_length = int(input("How long would you like the encrypted msg to be?: (int)"))

    while len(encrypt_list) < get_length:
        user_input = get_user_input()
        encrypt = abc_list.index(user_input)  
        encrypt_list.append(rot_list[encrypt])
    else:
        print("Your message has been encrypted: " + "".join(encrypt_list))
        

main()