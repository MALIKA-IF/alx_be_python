class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size):
        super.__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

class library:
    def __init__(self, books):
        self.books = books
        self.B=Book(self.title, self.author)
        self.E=EBook(self.title, self.author, self.file_size)
        self.P=PrintBook(self.title, self.author, self.page_count)

        def add_book(self, book):
            
            self.books = [self.B, self.E, self.P]
        

        def list_books(self):
            return self.books
        
mom = Library()
classic_book = Book("Pride and Prejudice", "Jane Austen")
mom.add_book(classic_book)
print(mom)     

        

        