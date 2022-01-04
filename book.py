from products import Product

class Book(Product):
    def __init__(self,  author, book, price, percent):
        self.author = author
        self.book = book
        self.price = float(price)
        self.final_price = self.percent(percent)

    def print(self):
        print(self.__str__())

    def __str__(self):
        return "Author: {} \t Book: {} Price {} - {}".format(self.author, self.book, self.price, self.final_price)
