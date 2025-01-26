class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"    

class EBook(Book):
    def __init__(self, title, author, file_size):
        super.__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{self.title} by {self.author}, size {self.file_size}"        

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    
    def __str__(self):
        return f"{self.title} by {self.author}, page {self.page_count}"       

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


        

        