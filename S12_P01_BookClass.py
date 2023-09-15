import random
import uuid

class Book:
    def __init__(self, bookId, bookName, bookPrice, bookAuthor, bookEdition):
        self.bookId = bookId
        self.bookName = bookName
        self.bookPrice = bookPrice
        self.bookAuthor = bookAuthor
        self.bookEdition = bookEdition

    

id = uuid.uuid4()
books = [
    Book(str(uuid.uuid4()), "To Kill a Mockingbird", 12.99, "Harper Lee", "50th Anniversary Edition"),
    Book(str(uuid.uuid4()), "1984", 10.99, "George Orwell", "First Edition"),
    Book(str(uuid.uuid4()), "The Great Gatsby", 14.95, "F. Scott Fitzgerald", "Revised Edition"),
    Book(str(uuid.uuid4()), "Pride and Prejudice", 9.99, "Jane Austen", "Collector's Edition"),
    Book(str(uuid.uuid4()), "The Catcher in the Rye", 11.99, "J.D. Salinger", "Classic Edition"),
    Book(str(uuid.uuid4()), "To the Lighthouse", 15.99, "Virginia Woolf", "Modern Library Edition"),
    Book(str(uuid.uuid4()), "Moby-Dick", 16.49, "Herman Melville", "Illustrated Edition"),
    Book(str(uuid.uuid4()), "The Hobbit", 8.99, "J.R.R. Tolkien", "75th Anniversary Edition"),
    Book(str(uuid.uuid4()), "The Odyssey", 11.50, "Homer", "Translated by Emily Wilson"),
    Book(str(uuid.uuid4()), "War and Peace", 22.95, "Leo Tolstoy", "Vintage Classics Edition"),
]


for i in books:
    # use : i.__dict__ to convert the dict
    print("{} | {:30} | {:5} | {:20} | {:30}".format(i.bookId,i.bookName,i.bookPrice,i.bookAuthor,i.bookEdition))