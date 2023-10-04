from lib.book import Book

# Get book properties 
def test_book_properties():
    book = Book(1, "Test Title", "Test Author Name")
    assert book.id == 1
    assert book.title == "Test Title"
    assert book.author_name == "Test Author Name"