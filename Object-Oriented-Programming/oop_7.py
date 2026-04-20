#aggregation: It is a special form of association where an object contains refrences to other objects. It represents a "has-a" relationship between the objects. In aggregation, the contained objects can exist independently of the container object.

class Library():

    number_of_books = 0

    def __init__(self, name):
        self.name = name
        self.book_list = []
    def add_book(self, book):
        self.book_list.append(book)

    def display_info(self):
        print("Library:", self.name)
        print("Number of Books:", Library.number_of_books)
        print("Books in Library:")
        for book in self.book_list:
            print("- {} by {}".format(book.title, book.author))

class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        Library.number_of_books += 1
    
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell") 

books = [book1, book2, book3]

library = Library("City Library")
for book in books:
    library.add_book(book)

library.display_info()
