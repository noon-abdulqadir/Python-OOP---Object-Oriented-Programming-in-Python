# Question 2
class Book():
    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.copies = copies
    
    def display(self):
        print(f"ISBN: {self.isbn}\nTitle: {self.title}\nPrice: {self.price}\nNumber of copies: {self.copies}")
    
# Question 3
    def in_stock(self):
        return self.copies > 0
    
    def sell(self):
        if self.in_stock():
            self.copies -= 1
            print(f'Sale of the book "{self.title}" is complete. {self.copies} copies of the book "{self.title}" remaining.')
        elif self.in_stock() == False:
            print(f'The book "{self.title}" is out of stock.')

# Question 5
    @property
    def price(self):
        return(self._price)
    
    @price.setter
    def price(self, new_price):
        if 50 <= new_price <= 1000:
            self._price = new_price
        else:
            raise(ValueError(f'The price of the book "{self.title}" cannot be less than 50 nor more than 1000.'))


book1 = Book('957-4-36-547417-1', 'Learn Physics', 'Stephen', 'CBC', 350, 200, 10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry', 'Jack', 'CBC', 400, 220, 20)
book3 = Book('957-7-39-347216-2', 'Learn Maths', 'John', 'XYZ', 500, 300, 5)
book4 = Book('957-7-39-347216-2', 'Learn Biology', 'Jack', 'XYZ', 400, 200, 6)

book1.display()

# Question 3
book1.in_stock()
book1.sell()

# Question 4
books = [book1,book2,book3,book4]

for book in books:
    book.display()

jacks_books = [book.title for book in books if book.author == "Jack"]
print(jacks_books)