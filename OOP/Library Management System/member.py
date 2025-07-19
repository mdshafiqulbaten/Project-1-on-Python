class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = {}

    def __str__(self):
        return f"Member ID: {self.member_id}, Name: {self.name}, Borrowed: {list(self.borrowed_books.keys())}"
