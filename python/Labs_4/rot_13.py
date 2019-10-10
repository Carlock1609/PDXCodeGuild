#! python3
# v2

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
    decrypted_list = []

    print("Welcome to rot 13!\nEnter in one letter at a time to be encrypted.")

    get_length = int(input("How long would you like the encrypted msg to be?: (int)"))

    while len(encrypt_list) < get_length:
        user_input = get_user_input()
        decrypted_list.append(user_input)
        encrypt = abc_list.index(user_input)  
        encrypt_list.append(rot_list[encrypt])
    else:
        print("\nYour message has been encrypted: " + "".join(encrypt_list))
        print("Your message decrypted is: " + "".join(decrypted_list))


def main2():
    rot_list = get_rot_list()
    abc_list = get_abc_list()
    encrypt_list = []
    decrypted_list = []
    user_input = get_user_input()

    for letter in user_input:
        if user_input in abc_list:
            encrypt_list.append(letter)

