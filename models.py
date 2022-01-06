from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, MetaData
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

Base = declarative_base()
engine = create_engine("postgresql+psycopg2://postgres:root@localhost/postgres_db")
session = Session(bind=engine)
Base.metadata.create_all(engine)


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer(), primary_key=True)
    author = Column(String(100), nullable=False)
    name = Column(String(300), nullable=False)
    price = Column(Float(), nullable=False)
    percent = Column(Float(), nullable=False)

    def __repr__(self):
        return "<Book (author=%s name='%s' price='%s')>" % (self.author, self.name, self.price)


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    surname = Column(String, nullable=True)
    telephone = Column(String(13), nullable=False)
    datetime = Column(DateTime, default=datetime.now)
    product = Column(Integer, ForeignKey('sweet.id'))


    def __repr__(self):
        chosen_sweet = session.query(Sweet).filter(Sweet.id == self.product).first()
        return '<Order(name=%s surname=%s telephone=%s product = %s)>' % \
               (self.name, self.surname, self.telephone, chosen_sweet)


class Sweet(Base):
    __tablename__ = 'sweet'
    id = Column(Integer,  primary_key=True)
    name = Column(String, nullable=False)
    weight = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    percent = Column(Float, nullable=False)
    orders = relationship("Order", backref="order")

    def __repr__(self):
        return "<Sweet(name='%s', weight='%s', price='%s')>" % (self.name, self.weight, self.price)

Base.metadata.create_all(engine)