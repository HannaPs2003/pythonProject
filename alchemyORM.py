# from sqlalchemy import create_engine, MetaData, Table, Integer, Float,\
#     String, Column, DateTime, ForeignKey, ForeignKeyConstraint
#
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import  mapper, Session, sessionmaker
#
# from datetime import datetime
#
#
# # class Sweet(object):
# #     pass
# class Book(object):
#     pass
# class Order(object):
#     pass
#
#
# class DB_ORM:
#     def __init__(self):
#         engine = create_engine("postgresql+psycopg2://postgres:root@localhost/postgres_db")
#         self.session = Session(bind=engine)
#         Base = declarative_base()
#         metadata = MetaData()
#
#
#         # self.sweet = Table('sweet', metadata,
#         #                       Column('id', Integer(), primary_key=True),
#         #                       Column('name', String(), nullable=False),
#         #                       Column('weight', Float(), nullable=False),
#         #                       Column('price', Float(), nullable=False),
#         #                       Column('percent', Float(), nullable=False)
#         #                    )
#
#         class Sweet(Base):
#             __tablename__='sweet'
#             id = Column(Integer(), primary_key=True)
#             name = Column(String(), nullable=False)
#             weight = Column(Float(), nullable=False)
#             price = Column(Float(), nullable=False)
#             percent = Column(Float(), nullable=False)
#
#
#         self.book = Table('book', metadata,
#                     Column('ID', Integer(), primary_key=True),
#                     Column('author', String(100), nullable=False),
#                     Column('name', String(100), nullable=False),
#                     Column('Price', Float, nullable=False),
#                     Column('percent', Float, nullable=False)
#                 )
#
#
#         self.order = Table('orders', metadata,
#                                Column('id', Integer(), primary_key=True, ),
#                                Column('name', String(), nullable=False),
#                                Column('surname', String(), nullable=False),
#                                Column('telephone', String()),
#                                Column('date_time', DateTime(), default=datetime.now),
#                                Column('product', Integer()),
#                                ForeignKeyConstraint(['product'], ['sweet.id']))
#         mapper(Sweet, self.sweet)
#         mapper(Book, self.book)
#         mapper(Order, self.order)
#
#         Base.metadata.create_all(engine)
#         print('ok')
#
#     def create_sweet(self):
#         s1 = Sweet(
#             id = 1,
#             name = 'tiktak',
#             weight = 100,
#             price = 100,
#             percent = 1.2,
#         )