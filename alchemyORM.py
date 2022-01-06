from sqlalchemy.ext.declarative import declarative_base
from models import Order, Sweet, Book
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

Base = declarative_base()

class DB_ORM:
    def __init__(self):
        self.engine = create_engine("postgresql+psycopg2://postgres:root@localhost/postgres_db")
        self.session = Session(bind=self.engine)
        # Base.metadata.create_all(self.engine)

    def add_db(self, new_line):
        self.session.add(new_line)
        print(self.session.new)
        self.session.commit()

    def create_sweet(self):
        name = input('VV name of sweet>>')
        weight = float(input('VV weight sweet>>'))
        price = float(input('VV sweet price>>'))
        new_sweet = Sweet(
            name=name,
            weight=weight,
            price=price,
            percent=1.2,
        )
        self.add_db(new_sweet)

    def read_sweet(self):
        print(self.session.query(Sweet).all())

    def delete_sweet(self):
        self.delete_order()
        self.session.query(Sweet).delete()
        print('sweets deleted')
        self.session.commit()

    def create_order(self):
        name = input('VV name of order>>')
        sur_name = input('VV surname of order>>')
        telephone = input('VV telephone of order>>')
        sweet_name = input('VV sweet name>>')
        chosen_sweet = self.session.query(Sweet).filter(Sweet.name == sweet_name).first()
        new_order = Order(
            name=name,
            surname=sur_name,
            telephone=telephone,
            product=chosen_sweet.id,
        )
        self.add_db(new_order)

    def read_order(self):
        print(self.session.query(Order).all())

    def delete_order(self):
        self.session.query(Order).delete()
        print('orders deleted')
        self.session.commit()

    # def create_book(self):
    #     author = input('VV author>>')
    #     book = input('VV book name>>')
    #     price = float(input('VV book price>>'))
    #     new_book = Book(
    #         author=author,
    #         name=book,
    #         price=price,
    #         percent=1.2,
    #     )
    #     self.add_db(new_book)