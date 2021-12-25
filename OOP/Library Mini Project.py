
# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# TahmidLibrary = Library(listofbooks , library_name)

# dictionary (books - nameofperson)

# create a main function and run an infinite while loop
# asking user for their input

class Library:
    def __init__(self,list_books,library_name):
        self.lend_data = {}
        self.list_books = list_books
        self.library_name = library_name

        for books in self.list_books:
            self.lend_data[books] = None
    def display_books(self):
        for index,book in enumerate(self.list_books):
            print(f"{index+1}){book}")

    def add_books(self,book_name):
        self.list_books.append(book_name)
        self.lend_data[book_name] = None
        print("Book is successfully added")

    def lend_book(self,book_name,author):
        if book_name in self.list_books:
            if self.lend_data[book_name] is None:
                self.lend_data[book_name] = author
                print("Book is successfully lended")
            else:
                print(f"Sorry this book is lended by {self.lend_data[book_name]}")
        else:
            print("You have written wrong book name")

    def return_book(self,book_name,author):
        if book_name in self.list_books:
            if self.lend_data[book_name]==author:
                self.lend_data.pop(book_name)
                print("Book is successfully returned")
            else:
                print("Sorry this book is not lended")
        else:
            print("You have written wrong book name")

    def delete_book(self,book_name):
        self.list_books.remove(book_name)
        self.lend_data.pop(book_name)
        print("Book is successfully deleted")

list_books = ["C++","Python","C Programming"]
secret_key = '123456'

Tahmid = Library(list_books,"Tahmid")
print(f"-------Welcome to {Tahmid.library_name}'s Library---------")
print(f"1)'d' for displaying book \n 2)'a' for add book \n 3)'l' for lending book \n 4)'r' for returning book \n 5)'del' for deleting book \n 6)'q' for exit ")
exit = False

while(exit is not True):

    inp = input("Enter any options:")
    if inp =='q':
        exit = True
    elif inp=='d':
        Tahmid.display_books()
    elif inp =='a':
        inp2 = input("Enter Book Name:")
        Tahmid.add_books(inp2)
    elif inp=='l':
        inp3 = input("Enter your name:")
        inp4 = input("Which book do you want to lend:")
        Tahmid.lend_book(inp4,inp3)
    elif inp =='r':
        inp3 = input("Enter your name:")
        inp4 = input("Which book do you want to return:")
        Tahmid.return_book(inp4,inp3)
    elif inp =='del':
        inp5 = input("Enter the secret key:")
        if inp5 ==secret_key:
            inp6 = input("Which book do you want to delete:")
            Tahmid.delete_book(inp6)
        else:
            print("You have entered wrong secret key")
    else:
        print("Invalid option.Try Again.")


