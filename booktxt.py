class Book:
    def __init__(self, book_id, title, author, genre, status):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.status = status


class Library:
    def __init__(self, filename):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    parts = line.strip().split("|")
                    if len(parts) >= 5:
                        book_id = int(parts[0])
                        title = parts[1]
                        author = parts[2]
                        genre = parts[3]
                        status = parts[4]
                        self.books.append(Book(book_id, title, author, genre, status))
        except Exception as e:
            print(f"Error loading books: {e}")

    def save_books(self):
        with open(self.filename, "w") as f:
            for book in self.books:
                line = "|".join([str(book.book_id), book.title, book.author, book.genre, book.status])
                f.write(line + "\n")

    def reserve_book(self, book_id, email):
        for book in self.books:
            if str(book.book_id) == str(book_id) and book.status == "Available":
                book.status = "Reserved"
                self.save_books()
                return True
        return False

    def cancel_reservation(self, book_id, email):
        for book in self.books:
            if str(book.book_id) == str(book_id) and book.status == "Reserved":
                book.status = "Available"
                self.save_books()
                return True
        return False
