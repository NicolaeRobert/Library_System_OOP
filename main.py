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
    def __init__(self,name,author,borrowed):
        self.name=name
        self.author=author
        self.borrowed=borrowed

    # The method that describes the book and the status of the book(can be borrowed or not)
    def describe_book(self):
        print(f"The book {self.name} is written by {self.author}.")
        if self.borrowed==True:
            print("It is currently in the possesion of the library and can be borrowed.")
        else:
            print("It is not currently in the possesion of the library and cannot be borrowed.")


