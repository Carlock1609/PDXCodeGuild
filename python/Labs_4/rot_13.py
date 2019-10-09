#! python3
# v1

import string

def get_abc_list():
    abc_list = list(string.ascii_lowercase)
    return abc_list

def get_rot_list():
    rot_list = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
    return rot_list

abc_list = get_abc_list()
rot_list = get_rot_list()

rot_list = abc_list
