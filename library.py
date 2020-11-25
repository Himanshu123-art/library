class Library:
    books=[]
    allocation={}
    def __init__(self):
        Library.books=["abc","php","c++","c","python","ruby","digital","electronics","computer","memory"]
    @classmethod
    def add_book(cls):
        book=input("enter the book name you want to ")
        cls.books.append(book)
    @classmethod
    def lend_book(cls):
        lend=input("enter the book you want to lend ")
        name = input("name of the holder ")
        if lend not in cls.books:
            if  lend in cls.allocation.keys():
                print("the book is already allocated to  ",cls.allocation[lend])
            else:
                print("the book name you entered is not available in the library")
        else:
            cls.books.remove(lend)
            cls.allocation[lend]=name
    @classmethod
    def display_book(cls):
        print("the following books are available in the library")
        print(cls.books)
    @classmethod
    def return_book(cls):
        rbook=input("enter the book you want to return  ")
        if rbook in cls.allocation.keys():
            del cls.allocation[rbook]
        cls.books.append(rbook)
def main():
    obj=Library()
    choice=1
    while choice:
        choicefun=int(input("enter 1 for adding book, 2 for lending, 3 for returing book, 4 for displaying book "))
        if choicefun==1:
            obj.add_book()
        elif choicefun==2:
            obj.lend_book()
        elif choicefun==3:
            obj.return_book()
        elif choicefun==4:
            obj.display_book()
        choice=int(input("if you want more operation press 1 else 0 to exit"))
main()



