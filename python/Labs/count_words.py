#! python3

# v2

# Finished translate()

import string

def get_opened_book():
    delete_list = "1234567890,.'!@#$%^&*()-[]/<>-\"=+_"
    replace_list = "                                  "

    open_book = open("C:\\Users\\jcyat\\Desktop\\book.txt", "r")
    read_book = open_book.read()
    clean_book = str.maketrans(delete_list, replace_list)
    cleaned_book = read_book.translate(clean_book)
    newbook = cleaned_book.lower().split()

    return newbook

def get_word_dict(mylist):
    word_dict = {}
    for i in mylist:
        if i not in word_dict:
            word_dict.update({i: 1})
        elif i in word_dict:
            word_dict[i] += 1
    return word_dict

def main(word_dict):
    words = list(word_dict.items())
    words.sort(key=lambda tup: tup[1], reverse=True)
    for i in range(min(10, len(words))):
        print(words[i])

main(get_word_dict(get_opened_book()))

