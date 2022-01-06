# from person import Person
# from datetime import datetime
# from products import Product



# class Order():
#     def __init__(self, name: str, surname: str, telephone: str, age: int, product: Product):
#         self.person = Person(name, surname, telephone, age)
#         self.product = product
#         self.created_date = datetime.now()
#
#
#
#     # @dec_printOr
#     def printOrder(self):
#         print(self.person, '\t', self.created_date, '\t', self.product)


# self.order = Table('orders', metadata,
#                    Column('id', Integer(), primary_key=True ),
#                    Column('name', String(), nullable=False),
#                    Column('surname', String(), nullable=False),
#                    Column('telephone', String()),
#                    Column('date_time', DateTime(), default=datetime.now),
#                    Column('product', Integer()),
#                    ForeignKeyConstraint(['product'], ['sweet.id']))


from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, MetaData
from datetime import datetime

Base = declarative_base()
# todo ForeignKey('sweet.id')
class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    surname = Column(String, nullable=True)
    telephone = Column(String(13), nullable=False)
    datetime = Column(DateTime, default=datetime.now)
    product = Column(Integer, ForeignKey('sweet.id'))

    def __repr__(self):
        return '<Order(name=%s surname=%s telephone=%s)>' % (self.name, self.surname, self.telephone)

