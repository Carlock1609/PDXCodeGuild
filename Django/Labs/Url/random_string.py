import random
import string

def random_gen():
    list_ele = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9',]
    code = ''
    counter = 0 
    while counter <= 8:
        code += random.choice(list_ele)
        counter += 1
    return code

random_gen()