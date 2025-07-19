from book import Book
from member import Member
from library import Library

def main():
    lib = Library()

    # Sample books and members
    lib.add_book(Book("B101", "1984", "George Orwell"))
    lib.add_book(Book("B102", "The Great Gatsby", "F. Scott Fitzgerald"))
    lib.add_book(Book("B103", "To Kill a Mockingbird", "Harper Lee"))

    lib.add_member(Member("M001", "Alice"))
    lib.add_member(Member("M002", "Bob"))

    # Menu
    while True:
        print("\nLibrary Menu:")
        print("1. List Books")
        print("2. List Members")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            lib.list_books()
        elif choice == '2':
            lib.list_members()
        elif choice == '3':
            mid = input("Enter Member ID: ")
            bid = input("Enter Book ID: ")
            lib.borrow_book(mid, bid)
        elif choice == '4':
            mid = input("Enter Member ID: ")
            bid = input("Enter Book ID: ")
            lib.return_book(mid, bid)
        elif choice == '5':
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
