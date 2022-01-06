# from products import Product



#
#
# class Sweet(Product):
#     def __init__(self, name, weight, price: float, percent):
#         self.name = name
#         self.weight = weight
#         self.price = price
#         self.final_price = self.percent(percent)
#
#     def print(self):
#         print(self.__str__())
#
#     def __str__(self):
#         return "{}\t{}\t{}\t{}".format(self.name, self.weight, self.price, self.final_price)

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey
Base = declarative_base()



class Sweet(Base):
    __tablename__ = 'sweet'
    id = Column(Integer,  primary_key=True)
    name = Column(String, nullable=False)
    weight = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    percent = Column(Float, nullable=False)
    # orders = relationship("Order")    #, backref = "order"

    def __repr__(self):
        return "<Sweet(name='%s', weight='%s', price='%s')>" % (self.name, self.weight, self.price)


