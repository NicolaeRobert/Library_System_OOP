from libraries import library1,library2,library3
from set_class_library import set_library
from classes import Reader

def choosen_library(library,reader):
    print(f"You have chosen the library: {library.name_of_library}")
    input_number=0
    message_for_operations=["1. Show books available in the library.",
                            "2. See the list of authors.",
                            "3. Borrow a book.",
                            "4. Return a book.",
                            "5. See the list of borrowed books.",
                            "6. Exit the program."
                            ]
    while input_number!=6:
        print("Operations to perform:")
        for i in message_for_operations:
            print(i)
        input_number=int(input("Your number: "))
        while input_number not in [1,2,3,4,5,6]:
            print("The number chosen doesn't respect the instructions. Introduce another one.")
            input_number=int(input("Your number: "))
        if input_number==1:
            library.show_books()
        elif input_number==2:
            for author in library.authors:
                print(author.name)
        elif input_number==3:
            print("Here is the list of available books. Choose one accoudingly to it's name:")
            print()
            library.show_books()
            print()
            book_name=input("Book name: ")
            book_object=library.return_book_object(book_name)
            if book_object==None:
                print("There is not any book with that name.")
            elif book_object.borrowed==True:
                print("This book has already been borrowed.")
            else:
                reader.borrow_book(book_object)
                print("The book has been borrowed successfully.")
        elif input_number==4:
            reader.see_borrowed_books()
            if len(reader.books_borrowed)!=0:
                print("Introduce the book that you want to return:")
                book_name=input("Book name: ")
                book_object=library.return_book_object(book_name)
                if book_object==None:
                    print("There is not any book with that name.")
                else:
                    reader.return_book(book_object)
                    print("The book has been returned.")
        elif input_number==5:
            reader.see_borrowed_books()
        
        print()

        

def main():
    libraries=[set_library(library1,"Library of Congress"),set_library(library2,"New York Public Library"),set_library(library3,"Boston Public Library")]

    print("Hello! Thank you for choosing out program of library sistem.")
    print("Before we start, please introduce you fullname")
    fullname=input("Fullnane: ")
    print()

    reader=Reader(fullname)

    print("Now that you have introduced your name we can start.")
    print("Below you have a list of the libraries that we represent:")
    print()

    print(f"1.{libraries[0].name_of_library}")
    print(f"2.{libraries[1].name_of_library}")
    print(f"3.{libraries[2].name_of_library}")
    print()

    print("Choose a numbert from 1 to 3 that represents the library that you choose and from where you want to borrow your book.")
    number=int(input("Your number is: "))
    
    while number not in [1,2,3]:
        print("The numbert introduces doesn't resprect the instructions.Introduce a new one.")
        number=int(input("Your number is: "))
    
    choosen_library(libraries[number-1],reader)

if __name__=="__main__":
    main()