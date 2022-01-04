from products import Product


class Sweet(Product):
    def __init__(self, name, weight, price: float, percent):
        self.name = name
        self.weight = weight
        self.price = price
        self.final_price = self.percent(percent)

    def print(self):
        print(self.__str__())

    def __str__(self):
        return "{}\t{}\t{}\t{}".format(self.name, self.weight, self.price, self.final_price)