class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books=[]

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        keep_books = []
        for item in self.books:
            if item.title != book.title or item.author != book.author:
                keep_books.append(item)
        self.books=keep_books
        return  self.books

    def search_books(self, search_string):
        results = []
        for item in self.books:
            if search_string.lower() in item.author.lower() or search_string.lower() in item.title.lower() :
                results.append(item)
        return results