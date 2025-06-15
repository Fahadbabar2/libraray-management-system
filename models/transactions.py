class Transaction:
    def __init__(self, user_id, book_id, borrow_date, due_date, returned=False, return_date=None):
        self.user_id = user_id
        self.book_id = book_id
        self.borrow_date = borrow_date
        self.due_date = due_date
        self.returned = returned
        self.return_date = return_date

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "book_id": self.book_id,
            "borrow_date": self.borrow_date,
            "due_date": self.due_date,
            "returned": self.returned,
            "return_date": self.return_date
        }
