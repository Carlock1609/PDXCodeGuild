#! python3 

# my_list = [1,2,3]
# print(len(my_list))

# class Sample():
#     pass

# my_sample = Sample()

# print((my_sample))

class Book():

    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages

    # USE THIS FOR DISPLAY
    # Printing the class Display_Board would print what the class is
    def __repr__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    # Gives output of variable given, otherwise it would just raise a error
    def __del__(self):
        print(f"A book object has been deleted")

b = Book(title="Python book",
        author="Jose",
        pages=200,)

print(len(b))

del b
print(b)