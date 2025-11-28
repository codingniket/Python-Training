class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def check_pages(self):
        if self.pages > 300:
            print(f"Book {self.title} has {self.pages} pages and is Eligible")
        else:
            print(f"Book {self.title} has {self.pages} pages and is Not Eligible")

x = Book("Joy of night", "John Doe", 360)
x.check_pages()