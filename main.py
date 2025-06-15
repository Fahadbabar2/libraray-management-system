from models.books import Book
from models.users import User
from services.book_service import add_book, list_books, search_book
from services.user_service import add_user, list_users, remove_user
from services.transaction import borrow_book, return_book

def menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Search Book by Title")
    print("4. Add User")
    print("5. List Users")
    print("6. Remove User")
    print("7. Borrow Book")
    print("8. Return Book")
    print("9. Exit")

def main():
    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            try:
                book_id = int(input("Book ID: "))
                title = input("Title: ")
                author = input("Author: ")
                copies = int(input("Copies: "))
                book = Book(book_id, title, author, copies)
                add_book(book)
            except ValueError:
                print("Invalid input. Please enter numbers where required.")

        elif choice == "2":
            list_books()

        elif choice == "3":
            title = input("Enter title to search: ")
            search_book(title)

        elif choice == "4":
            try:
                user_id = int(input("User ID: "))
                name = input("User name: ")
                user = User(user_id, name)
                add_user(user)
            except ValueError:
                print("Invalid user ID")

        elif choice == "5":
            list_users()

        elif choice == "6":
            try:
                user_id = int(input("Enter User ID to remove: "))
                remove_user(user_id)
            except ValueError:
                print("Invalid user ID")

        elif choice == "7":
            try:
                user_id = int(input("Your User ID: "))
                book_id = int(input("Book ID to borrow: "))
                borrow_book(user_id, book_id)
            except ValueError:
                print("Invalid input")

        elif choice == "8":
            try:
                user_id = int(input("Your User ID: "))
                book_id = int(input("Book ID to return: "))
                return_book(user_id, book_id)
            except ValueError:
                print("Invalid input")

        elif choice == "9":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
