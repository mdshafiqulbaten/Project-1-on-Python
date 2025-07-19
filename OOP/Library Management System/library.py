from datetime import datetime, timedelta

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.book_id] = book

    def add_member(self, member):
        self.members[member.member_id] = member

    def borrow_book(self, member_id, book_id):
        member = self.members.get(member_id)
        book = self.books.get(book_id)
        if not member or not book:
            print("Invalid member or book ID")
            return
        if book.is_borrowed:
            print("Book is already borrowed")
            return
        book.is_borrowed = True
        due_date = datetime.now() + timedelta(days=14)
        member.borrowed_books[book_id] = due_date
        print(f"{book.title} borrowed by {member.name}. Due on {due_date.strftime('%Y-%m-%d')}")

    def return_book(self, member_id, book_id):
        member = self.members.get(member_id)
        book = self.books.get(book_id)
        if not member or not book:
            print("Invalid member or book ID")
            return
        if book_id not in member.borrowed_books:
            print("This book was not borrowed by the member")
            return
        due_date = member.borrowed_books.pop(book_id)
        book.is_borrowed = False
        returned_date = datetime.now()
        if returned_date > due_date:
            print("Book is returned late. A fine may be applied.")
        print(f"{book.title} returned by {member.name} on {returned_date.strftime('%Y-%m-%d')}")

    def list_books(self):
        for book in self.books.values():
            print(book)

    def list_members(self):
        for member in self.members.values():
            print(member)
