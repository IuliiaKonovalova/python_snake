class Book:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content
        self.last_page = 0

    def display_page(self):
        return self.content[self.last_page]
    
    def turn_page(self):
        if self.last_page < len(self.content) - 1:
            self.last_page += 1
        else:
            self.last_page = 0


class Library:
    def __init__(self):
        self.collection = dict()
        self.active_book = None
        self.id_counter = 0

    def add_book(self, title, content):
        mew_book = Book(self.id_counter, title, content)
        self.collection[mew_book.id] = mew_book
        self.id_counter += 1

    def remove_from_collection(self, book_id):
        del self.collection[book_id]

    def set_active_book(self, book_id):
        self.active_book = self.collection[book_id]

    def display_page(self):
        return self.collection[self.active_book].display_page()
    
    def turn_page(self):
        self.collection[self.active_book].turn_page()