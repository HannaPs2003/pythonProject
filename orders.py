from person import Person
# from products import Product
from datetime import datetime
from products import Product

persons = []


def dec_printOr(func):
    def wrapper(*args, **kwargs):
        print('List of orders')
        func(*args, **kwargs)
    return wrapper

def printAll():
    for item in persons:
        print(item)


class Order():
    def __init__(self, name: str, surname: str, telephone: str, age: int, product: Product):
        self.person = Person(name, surname, telephone, age)
        self.product = product
        persons.append(self.person)
        self.created_date = datetime.now()



    # @dec_printOr
    def printOrder(self):
        print(self.person, '\t', self.created_date, '\t', self.product)


