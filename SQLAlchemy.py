import orders

from sqlalchemy import create_engine, MetaData, Table, Integer, Float,\
    String, Column, DateTime, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import mapper
from datetime import datetime
from sqlalchemy import select, delete
from sweets import Sweet
from orders import Order


metadata = MetaData()

class EngineDb:
    def __init__(self):
        engine = create_engine("postgresql+psycopg2://postgres:root@localhost/postgres_db")
        engine.connect()

        # todo i have some problems with ID
        self.book = Table('book', metadata,
            Column('ID', Integer(), primary_key=True),
            Column('author', String(100), nullable=False),
            Column('name', String(100), nullable=False),
            Column('Price', Float, nullable=False),
            Column('percent', Float, nullable=False)
        )

        self.sweet = Table('sweet', metadata,
                      Column('id', Integer(), primary_key=True),
                      Column('name', String(), nullable=False),
                      Column('weight', Float(), nullable=False),
                      Column('price', Float(), nullable=False),
                      Column('percent', Float(), nullable=False)
        )
        self.orders = Table('orders', metadata,
                       Column('id', Integer(), primary_key=True, ),
                       Column('name', String(), nullable=False),
                       Column('surname', String(), nullable=False),
                       Column('telephone', String()),
                       Column('date_time', DateTime(), default=datetime.now),
                       Column('product', Integer()),
                       ForeignKeyConstraint(['product'], ['sweet.id']))


        metadata.create_all(engine)
        self.conn = engine.connect()

    def add_sweet(self, sweet):
        all_sweets = select(self.sweet)
        r = self.conn.execute(all_sweets)
        inc = r.rowcount + 1
        # name = input('VV name of sweet>>')
        # weight = float(input('VV weight sweet>>'))
        # price = float(input('VV sweet price>>'))

        # sweet = Sweet(id=inc, name=name, weihgt=weight, price=price, percent=persent)

        new_sweet = self.sweet.insert().values(
            id=inc,
            name=sweet.name,
            weight=sweet.weight,
            price=sweet.price,
            percent=sweet.final_price,
        )
        print(new_sweet.compile().params)
        r = self.conn.execute(new_sweet)

        print('------------')
        # self.read_sweets()
        # self.add_order()

    def read_sweets(self):
        all_sweets = select(self.sweet)
        r = self.conn.execute(all_sweets)
        print('{:10} \t {:10} \t {:10} \t {:10}'.format('name', 'weight', 'price', 'full price'))
        for row in r:
            id, name, weight, price, full_price = row
            print("{:10} \t {:10} \t {:10} \t {:10}".format(name, weight, price, full_price))

    def delete_sweets(self):
        self.delete_orders()
        del_sweets = delete(self.sweet)
        self.conn.execute(del_sweets)
        print('sweet products deleted')


    def add_order(self):
        name = input('VV name of order>>')
        sur_name = input('VV surname of order>>')
        telephone = input('VV telephone of order>>')
        age = int(input('VV age of order>>'))
        sweet_name = input('VV sweet name>>')
        r = select([self.sweet]).\
            where(self.sweet.c.name == sweet_name)
        r = self.conn.execute(r)
        for row in r:
            id_s, name_s, weight, price, full_price = row
            product = Sweet(name_s, weight, price, full_price)
            print("{:10} \t {:10} \t {:10} \t {:10}".format(name_s, weight, price, full_price))
        order = Order(name, sur_name, telephone, age, product)
        # order.printOrder()
        query = select([self.orders])
        r = self.conn.execute(query)
        inc = r.rowcount + 1
        new_order = self.orders.insert().values(
            id = inc,
            name = order.person.name,
            surname = order.person.surname,
            telephone = order.person.telephone,
            date_time = order.created_date,
            product = id_s,
        )
        r = self.conn.execute(new_order)
        # self.read_orders()

    def read_orders(self):
        r = self.conn.execute(select(self.orders))
        for line in r:
            id_o, name_o, sur_name_o, telephone_o, date_time_o, product_o = line
            s = self.conn.execute(select([self.sweet]).where(self.sweet.c.id == int(product_o)))
            for row in s:
                id_s, name_s, weight, price, full_price = row
                # print("{:10} \t {:10} \t {:10} \t {:10}".format(name_s, weight, price, full_price))
            print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(name_o, sur_name_o, telephone_o, date_time_o, name_s, weight, price, full_price))



    def delete_orders(self):
        self.conn.execute(delete(self.orders))
        print('orders deleted')


        # some_sweets = select([sweet.c.name, sweet.c.id]).where(
        #     sweet.c.id < 10
        # )
        # r = conn.execute(some_sweets)
        # for row in r:
        #     print(row)
        #
        # r = delete(sweet).where(
        #     sweet.c.name.like('2%')
        # )
        #
        # rs = conn.execute(r)
        #
        # some_sweets = select([sweet.c.name, sweet.c.id]).where(
        #     sweet.c.id < 10
        # )
        # r = conn.execute(some_sweets)
        # for row in r:
        #     print(row)





