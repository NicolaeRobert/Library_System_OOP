# The class Author represents the author of a book or of a series of books
class Author:
    # The constructor of the Author class
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        books=[]
    
    # The metod that allows us to add books
    def add_book(self,book):
        self.books.append(book)
    
    # The method that shows the books of the author
    def show_book(self):
        # Check to see if there are any books written by this author
        if len(self.books)==0:
            print(f"The author {self.first_name} {self.last_name} has no books written")
        else:
            print(f"The author {self.first_name} {self.last_name} has written these books:")
            for book in self.books:
                print(book)# Aici trebuie sa zic book.name ca sa afiseza numele cartii

# The class Book represents a book
class Book:
    # The constructor of the Book class
    def __init__(self,name,author):
        self.name=name
        self.author=author
        self.borrowed=False

    # The method that describes the book and the status of the book(can be borrowed or not)
    def describe_book(self):
        print(f"The book {self.name} is written by {self.author}.")
        if self.borrowed==True:
            print("It is currently in the possesion of the library and can be borrowed.")
        else:
            print("It is not currently in the possesion of the library and cannot be borrowed.")

# The Reader class
class Reader:
    # The constructor of the Reader class
    def __init__(self,first_name,last_name):
        self.firs_name=first_name
        self.last_name=last_name
        self.books_borrowed=[]

    # The method that allows a reader to borrow a book
    def borrow_book(self,book):
        self.books_borrowed.append(book)
        book.borrowed=True

    # The method that allows a reader to return a book
    def return_book(self,book):
        book.borrowed=False
        self.books_borrowed.pop(book)
    
    # The method that allws a user to see all of the borrowed books if there are any
    def see_borrowed_books(self):
        if len(self.books_borrowed)==0:
            print("There isn't any book borrowed.")
        else:
            print("The books that are borrowed are:")
            for book in self.books_borrowed:
                print(book.name)

# The Library class
class Library:
    # The constructor of the Library class
    def __init__(self,name):
        self.name_of_library=name
        self.authors=[]
        self.books=[]

    # The method that returns a book object according to the name, or None if the object doesn't exists
    def return_book_objects(self,name):
        for book in self.books:
            if book.name==name:
                return book
        return None
    
    # The method that prints all the books available in the library
    def show_book(self):
        print("These are the books available in the library")
        for book in self.books:
            print(book.name)