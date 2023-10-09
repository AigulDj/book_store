class Book:
    def __init__(self, id, title, author_name):
        self.id = id 
        self.title = title
        self.author_name = author_name

    def __eq__(self, other):
        return (
            isinstance(other, Book) and
            self.id == other.id and
            self.title == other.title and
            self.author_name == other.author_name
        )

    def __repr__(self):
        return f"{self.id} - {self.title} - {self.author_name}"
    
