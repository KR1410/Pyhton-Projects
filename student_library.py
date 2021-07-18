class Library:
    def __init__(self, listofbooks):
        self.books = listofbooks

    def available_books(self):
        print("Books present in the library are: ")
        for books in self.books:
            print(" # " + books)

    def borrow(self, bookname):
        if bookname in self.books:
            print(f"{bookname} books has been issued. Please keep it safe and return it within 30 days to avoid the fine")
            (self.books).remove(bookname)
        else:
            print("Sorry, Book either is already issued or not present in the library")

    def return_book(self, bookname, original_collection):
        if bookname in self.books:
            print("This book is not from our library")
        elif bookname in original_collection:
            (self.books).append(bookname)
            print("thank  you")
        else:
            print("this book does not belong to this library")

class Student:
    def request_book(self):
        self.book = input("enter the name of the book: ")
        return self.book

    def return_book(self):
        self.book = input("enter the name of the book: ")
        return self.book

if __name__ == "__main__":
    central_library = Library(["AI", "DSA", "Python", "C++", "Ethical Hacking", "Android Development"])
    present_books = ["AI", "DSA", "Python", "C++", "Ethical Hacking", "Android Development"]

    KR = Student()

    while(True):
        greetings = ''' "Welcome to Central Library"
        Kindly choose an option:
        1. List all the books
        2. Request a book
        3. Return a book
        4. Exit the Library
        '''
        
        print(greetings)
        a = int(input("enter a choice: "))
        if a == 1:
            central_library.available_books()
        elif a == 2:
            central_library.borrow(KR.request_book())
        elif a == 3:
            central_library.return_book(KR.return_book(),present_books)
        elif a == 4:
            print("thank you")
            exit()
        else:
            print("Invaid Choice!!!!!!!!!!!!!!!!!!!!!!!")
            print("try it again")

