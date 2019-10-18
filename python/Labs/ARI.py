#! python3

#v1 DONE!

import string

def get_book():
    delete_list = " 1234567890,.'!@#$%^&*()-[]/<>-\"=+_"
    replace_list = "                                   "
    open_book = open("C:\\Users\\jcyat\\Desktop\\book3.txt", "r")
    read_book = open_book.read()
    clean_book = str.maketrans(delete_list, replace_list)
    cleaned_book = read_book.translate(clean_book)
    book = cleaned_book.lower().split()
    return book

def get_book_words(book):
    word_count = 0
    for i in book:
        word_count += 1
    return word_count

def get_book_chars(book):
    char_count = 0
    for i in book:
        for i in i:
            char_count += 1
    return char_count

def get_book_sentences():
    # cannot use get_book since delete_lsit is different
    delete_list = " 1234567890,'@#$%^&*()-[]/<>-\"=+_!?"
    replace_list = "                                 .."
    open_book = open("C:\\Users\\jcyat\\Desktop\\book3.txt", "r")
    read_book = open_book.read()
    clean_book = str.maketrans(delete_list, replace_list)
    cleaned_book = read_book.translate(clean_book)
    book = cleaned_book.split(".")

    sentence_count = 0
    for i in book:
        sentence_count += 1
    return sentence_count

def get_ARI_formula(word_count, char_count, sentence_count):
    ari_results = round(((4.71*(char_count/word_count)) + (0.5*(word_count/sentence_count))) - 21.43)

    if ari_results < 1:
        ari_results = 1
    if ari_results > 14:
        ari_results = 14
    return ari_results

def main():
    ari_scale = {
        1: {"ages": "5-6", "grade_level": "Kindergarten"},
        2: {"ages": "6-7", "grade_level": "1st Grade"},
        3: {"ages": "7-8", "grade_level": "2nd Grade"},
        4: {"ages": "8-9", "grade_level": "3rd Grade"},
        5: {"ages": "9-10", "grade_level": "4th Grade"},
        6: {"ages": "10-11", "grade_level": "5th Grade"},
        7: {"ages": "11-12", "grade_level": "6th Grade"},
        8: {"ages": "12-13", "grade_level": "7th Grade"},
        9: {"ages": "13-14", "grade_level": "8th Grade"},
        10: {"ages": "14-15", "grade_level": "9th Grade"},
        11: {"ages": "15-16", "grade_level": "10th Grade"},
        12: {"ages": "16-17", "grade_level": "11th Grade"},
        13: {"ages": "17-18", "grade_level": "12th Grade"},
        14: {"ages": "18-22", "grade_level": "College"},
    }
    ARI_result = get_ARI_formula(get_book_words(get_book()), get_book_chars(get_book()), get_book_sentences())
    
    print(f'The ARI for book2.txt is {ARI_result}\nThis corresponds to a {ari_scale[ARI_result]["grade_level"]}\nThat is suitable for an average person {ari_scale[ARI_result]["ages"]} years old')

main()

