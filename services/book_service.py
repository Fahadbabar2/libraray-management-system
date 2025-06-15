from models.books import Book  # ✅ Correct
import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'books.json')

def load_books():
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, 'r') as f:
        return json.load(f)

def save_books(books):
    with open(DATA_PATH, 'w') as f:
        json.dump(books, f)

def add_book(book):
    books = load_books()
    for b in books:
        if b['book_id'] == book.book_id:
            print("Book ID already exists")
            return
    books.append(book.to_dict())
    save_books(books)
    print("Book added successfully")

def list_books():
    books = load_books()
    if not books:
        print("No books found")
        return
    for b in books:
        print("ID:", b['book_id'], "Title:", b['title'], "Author:", b['author'], "Copies:", b['copies'])

def search_book(title):
    books = load_books()
    found = False
    for b in books:
        if title.lower() in b['title'].lower():
            print("ID:", b['book_id'], "Title:", b['title'], "Author:", b['author'], "Copies:", b['copies'])
            found = True
    if not found:
        print("No book found with that title")
