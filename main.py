
from products import Product
from orders import Order, printAll
from sweets import Sweet
from book import Book
from SQLAlchemy import EngineDb
# from alchemyORM import DB_ORM


def changePercent():
    return float(input('VV percent to price>>'))

db_engine = EngineDb()
products = []
percent = changePercent()



def commands(comd):
    global percent
    if comd == 'info':
        info()
    # if comd == 'addProductBook':
    #     addProductBook()
    if comd == 'addProductSweet':
        addProductSweet()
    if comd == 'printProducts':

        db_engine.read_sweets()
    if comd == 'printOrders':
        db_engine.read_orders()
    if comd == 'delOrders':
        db_engine.delete_orders()
    if comd == 'addOrder':
        db_engine.add_order()
    if comd == 'changePercent':
        global percent
        percent = changePercent()
    if comd == 'delProducts':
        db_engine.delete_sweets()



def info():
    print('info - for watch information of commands')
    # print('addProductBook - for add book on product')
    print('addProductSweet - for add sweet on product')
    print('printProducts - for print all products in the list')
    print('delProducts - for clear DB PRODUCTS and ORDERS')
    print('----------------------------------------------------')
    print('addOrder - for add order on orders')
    print('printOrders - for print all orders in the list')
    print('delOrders - for clear DB ORDERS')

    # print('changePercent - for change percent of price')



def addProductBook():
    global percent
    author = input('VV author>>')
    book = input('VV book name>>')
    price = float(input('VV book price>>'))
    product_book = Book(author, book, price, percent)
    product_book.price = price
    # product.print()

    products.append(product_book)



def addProductSweet():
    name = input('VV name of sweet>>')
    weight = float(input('VV weight sweet>>'))
    price = float(input('VV sweet price>>'))
    product_sweet = Sweet(name, weight, price, percent)
    product_sweet.price = price
    # product.print()

    products.append(product_sweet)
    # db_engine.add_sweet(product_sweet)


# dbORM = DB_ORM()


while True:
    command = input("VV command:>>")
    commands(command)



