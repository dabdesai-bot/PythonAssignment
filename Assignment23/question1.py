class BookStore:
    NoOfBooks = 0   # class variable

    def __init__(self, name, author):
        self.Name = name
        self.Author = author
        BookStore.NoOfBooks=  BookStore.NoOfBooks + 1

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books: {BookStore.NoOfBooks}")
                                                            

Obj1 = BookStore("Linux System programming","Robert Love")
Obj1.Display()   


Obj2 = BookStore("Python Programming","Guido Van Rossum")
Obj2.Display() 
     

