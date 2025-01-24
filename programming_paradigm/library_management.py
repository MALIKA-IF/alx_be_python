class Book:
  def __init__(self,title,author):
     self.title=title
     self.author=author
     self._is_checked_out=False

  def check_out(self):
    if not self._is_checked_out:
       self._is_checked_out=True
       return True
    return False  
     
  def return_book(self):
    if self._is_checked_out:
       self._is_checked_out=False
       return False
    return False
  def is_available(self):
    return not self._is_checked_out

class Library:
  def __init__(self):
    self._books = []

  def add_book(self, book):
    self._books.append(book)  

  def check_out_book(self, title):
    for book in self._books:
      if book.title == title and book.is_available():
        book.check_out()
        print(f"book {title}, checked our succefully")
        return True
    print(f"book {title} is not available")    

  def return_book(self,title):
    for book in self._books:
      if book.title == title and not book.is_available():
          book.return_book()
          print(f"book{title}, is returned successfully")
          return True
    print(f"book{title}, not checked out")
    return False
  def list_available_books(self):
    for book in self._books:
       if book.is_available():
          available_books=[book]
   # if available_books:
   #   for book in available_books:
          print(f"Title: {book.title}, Author: {book.author}")
       else:
        print("No Books")  




