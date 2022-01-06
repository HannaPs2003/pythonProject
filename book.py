# from products import Product
#
# class Book(Product):
#     def __init__(self,  author, book, price, percent):
#         self.author = author
#         self.book = book
#         self.price = float(price)
#         self.final_price = self.percent(percent)
#
#     def print(self):
#         print(self.__str__())
#
#     def __str__(self):
#         return "Author: {} \t Book: {} Price {} - {}".format(self.author, self.book, self.price, self.final_price)
#

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer(), primary_key=True)
    author = Column(String(100), nullable=False)
    name = Column(String(300), nullable=False)
    price = Column(Float(), nullable=False)
    percent = Column(Float(), nullable=False)

    def __repr__(self):
        return "<Book (author=%s name='%s' price='%s')>" % (self.author, self.name, self.price)



