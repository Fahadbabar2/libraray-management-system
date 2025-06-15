import json
import os
from datetime import datetime, timedelta

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'transactions.json')

def load_transactions():
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, 'r') as f:
        return json.load(f)

def save_transactions(transactions):
    with open(DATA_PATH, 'w') as f:
        json.dump(transactions, f)

def borrow_book(user_id, book_id):
    transactions = load_transactions()
    for t in transactions:
        if t['book_id'] == book_id and not t.get('returned', False):
            print("Book is already borrowed")
            return
    due_date = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')
    transaction = {
        'user_id': user_id,
        'book_id': book_id,
        'borrow_date': datetime.now().strftime('%Y-%m-%d'),
        'due_date': due_date,
        'returned': False
    }
    transactions.append(transaction)
    save_transactions(transactions)
    print("Book borrowed, due on", due_date)

def return_book(user_id, book_id):
    transactions = load_transactions()
    for t in transactions:
        if t['user_id'] == user_id and t['book_id'] == book_id and not t.get('returned', False):
            t['returned'] = True
            t['return_date'] = datetime.now().strftime('%Y-%m-%d')
            save_transactions(transactions)
            print("Book returned successfully")
            return
    print("No active borrow record found for this book and user")
