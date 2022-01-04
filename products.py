from abc import ABC


class Product(ABC):

    def __init__(self):
        self.price = 100

    def percent(self, percent):
        return self.price * percent

    def printProduct(self):
        print(self.__str__())

    def __str__(self):
        return "{}".format(self.price)


