import psycopg2
from psycopg2 import Error
from book import Book
from sweets import Sweet


class DB:
    def __init__(self):
        self.connection = psycopg2.connect(user="postgres",
                                      password="root",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="postgres_db")
        self.cursor = self.connection.cursor()

    # todo finalPrice price * percenr * (price?)
    def createBook(self, book):
        self.cursor.execute("select * from book")
        tempvar = self.cursor.fetchall()
        inc = len(tempvar)
        self.cursor.execute(" INSERT INTO book (ID, author, name, PRICE, percent) VALUES (%s, %s, %s, %s, %s)",
                       (inc, book.author, book.book, book.price, book.final_price))
        print(book.final_price)
        self.connection.commit()
        self.readBook()

    def deleteBook(self):
        delete_query = """Delete from book"""
        self.cursor.execute(delete_query)
        self.connection.commit()
        count = self.cursor.rowcount
        print(count, "Запись успешно удалена")
        self.readBook()


    def readBook(self, percent):
        self.cursor.execute("SELECT * from book")
        record = self.cursor.fetchall()
        for line in record:
            book_id, book_author, book_name, book_price, book_percent = line
            new_book_product = Book(book_author, book_name, book_price, percent)
            print(new_book_product)
            print(book_percent)


    # def createTableSweets(self):
    #     create_table_query = '''create table sweet
    #                             (id int primary key not null,
    #                             name text not null,
    #                             weight real,
    #                             price real not null,
    #                             percent real);'''
    #     self.cursor.execute(create_table_query)
    #     self.connection.commit()
    #     print('Table sweet create')

    def createSweet(self, sweet):
        self.cursor.execute("select * from sweet")
        tempvar = self.cursor.fetchall()
        inc = len(tempvar)
        self.cursor.execute("insert into sweet (id, name, weight, price, percent) values (%s, %s, %s, %s, %s)",
                            (16, sweet.name, sweet.weight, sweet.price, sweet.final_price))
        self.connection.commit()

    def readSweet(self, percent):
        self.cursor.execute("select * from sweet")
        record = self.cursor.fetchall()
        for line in record:
            sweet_id, sweet_name, sweet_weight, sweet_price, sweet_percent = line
            new_sweet_product = Sweet(sweet_name, sweet_weight, sweet_price, percent)
            print(new_sweet_product)

    def deleteSweet(self):
        self.cursor.execute("delete from sweet")
        self.connection.commit()


    def __enter__(self):
        return self.cursor

    def __exit__(self, type, value, traceback):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Соединение с PostgreSQL закрыто")