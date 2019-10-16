#! python3

# v1
# new loop for replace2

#REMOVE PUNCS FROM TXTS
# Try for looping over .strip() or replace()
# Try making a var with string.ascii_letters and check if in
# Learn .translate()

def get_opened_book():
    open_book = open("C:\\Users\\jcyat\\Desktop\\book.txt", "r")
    read_book = open_book.read().replace("'", "")
    newbook = read_book.lower().split()

        

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

# # word_dict is a dictionary where the key is the word and the value is the count
# words = list(word_dict.items()) # .items() returns a list of tuples
# words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
# for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
#     print(words[i])