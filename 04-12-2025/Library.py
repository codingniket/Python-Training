class Library:
    def __init__(self):
        self.books = {}

    def add(self, title, author):
        self.books[title] = author
        print(f"'{title}' by {author} added to library")

    def show_books(self):
        print("Books in library:")
        for title, author in self.books.items():
            print(f"{title} by {author}")

    def search_book(self, keyword):
        found = False
        for title, author in self.books.items():
            if keyword.lower() in title.lower() or keyword.lower() in author.lower():
                print(f"Found: {title} by {author}")
                found = True
        if not found:
            print("No matching book found")


# Example usage
lib = Library()
lib.add("Dracula", "Bram Stoker")
lib.add("Frankenstein", "Mary Shelley")

lib.show_books()
lib.search_book("Bram")
lib.search_book("Dracula")