
from products import Product
from orders import Order, printAll
from sweets import Sweet
from book import Book
from db import DB
from SQLAlchemy import EngineDb
from iterator import Iterator


def changePercent():
    return float(input('VV percent to price>>'))

db_engine = EngineDb()
products = []
percent = changePercent()
db = DB()
# db.createTableSweets()

def commands(comd):
    global percent
    if comd == 'info':
        info()
    # if comd == 'addProductBook':
    #     addProductBook()
    if comd == 'addProductSweet':
        addProductSweet()
    if comd == 'printProducts':
        # with DB() as cursor:
        #     print('\n------------------')
        #     db.readBook(percent)
        #     print('------------------')
            # db.readSweet(percent)
        db_engine.read_sweets()
    if comd == 'printOrders':
        db_engine.read_orders()
    if comd == 'delOrders':
        db_engine.delete_orders()
    if comd == 'addOrder':
        db_engine.add_order()
    # if comd == 'changePercent':
    #     global percent
    #     percent = changePercent()
    if comd == 'delProducts':
        # with DB() as cursor:
            # db.deleteBook()
            # db.deleteSweet()
        db_engine.delete_sweets()


# todo менеджеры контекста Python


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
    with DB() as cursor:
        db.createBook(product_book)


def addProductSweet():
    name = input('VV name of sweet>>')
    weight = float(input('VV weight sweet>>'))
    price = float(input('VV sweet price>>'))
    product_sweet = Sweet(name, weight, price, percent)
    product_sweet.price = price
    # product.print()

    products.append(product_sweet)
    # with DB() as cursor:
    #     db.createSweet(product_sweet)
    db_engine.add_sweet(product_sweet)

# addProductBook()
# addProductSweet()
# print('------------')
##############################################
# myclass = Iterator(len(products), products)
# productI = iter(myclass)
##############################################
# print(next(productI))

# for x in productI:
#     print(x)


# print('Hello. we start')
# a = Order('anna', 'pstyga', '+7589890809578', 18, products[1])
# a.printOrder()
# b = Order('Hanna', 'Ps', '+3456789009876', 15, products[1])
# b.printOrder()
# c = Order('Annatolia', '-', '+1234567890987', 20, products[1])
# c.printOrder()
# print('-------------------')
# printAll()



while True:
    command = input("VV command:>>")
    commands(command)



