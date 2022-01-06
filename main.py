from alchemyORM import DB_ORM

dbORM = DB_ORM()

def commands(comd):
    if comd == 'info':
        info()
    if comd == 'addProductBook':
        dbORM.create_book()
    if comd == 'addProductSweet':
        dbORM.create_sweet()
    if comd == 'printProducts':
        dbORM.read_sweet()
    if comd == 'printOrders':
        dbORM.read_order()
    if comd == 'addOrder':
        dbORM.create_order()
    if comd == 'delProducts':
        dbORM.delete_sweet()

def info():
    print('info - for watch information of commands')
#     # print('addProductBook - for add book on product')
    print('addProductSweet - for add sweet on product')
    print('printProducts - for print all products in the list')
    print('delProducts - for clear DB PRODUCTS and ORDERS')
    print('----------------------------------------------------')
    print('addOrder - for add order on orders')
    print('printOrders - for print all orders in the list')

while True:
    command = input("VV command:>>")
    commands(command)



