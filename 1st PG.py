class book:
    def __init__(self,book_title,author_name,price):
        self.book_title=book_title
        self.author_name=author_name
        self.price=price
    def display_books(self):
        print("Book Name :",self.book_title)
        print("Author :",self.author_name)
        print("Price : ₹",self.price)
disp=book("Rich Dad Poor Dad","Robert T. Kiyosaki",129)
disp.display_books()