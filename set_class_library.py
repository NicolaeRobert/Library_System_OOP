from classes import Author,Book,Library

def set_library(authors_and_books,library_name):

    # Create two empty lists that will hold the objects for Author and Book
    list_of_authors=[]
    list_of_books=[]

    # Here we iterate through the data received and create the object that corespond to the author and book
    for iterable in authors_and_books:
        list_of_authors.append(Author(iterable["author"]))

        for book in iterable["books"]:
            list_of_books.append(Book(book,iterable["author"]))

    # Create the library object and then initialize it so that is has books and authors in it
    library_object=Library(library_name)
    library_object.authors=list_of_authors
    library_object.books=list_of_books

    # Return the library object
    return library_object

