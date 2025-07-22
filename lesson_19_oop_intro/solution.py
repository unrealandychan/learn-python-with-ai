
# Lesson 19: Solution

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_summary(self):
        return f"'{self.title}' by {self.author} is {self.pages} pages long."

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Dune", "Frank Herbert", 412)

print(book1.get_summary())
print(book2.get_summary())
