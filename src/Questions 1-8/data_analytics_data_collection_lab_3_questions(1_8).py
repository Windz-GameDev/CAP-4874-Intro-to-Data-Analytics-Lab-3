"""
    Title: Data Analytics Lab 3: Data Collection (Questions 1 - 8)
    Author: Aaron Goldstein
    Date: 2/25/2023
    Github Repo: https://github.com/Windz-GameDev/Data-Analytics-Lab-3

    The purpose of this program is to create a simple sqlite3 database for a business.
    After establishing a connection, it creates tables for customers, orders, products, and sales.
    Afterwards, it inserts sample data into each table, which is then selected, and queried upon. Finally, it
    updates the sales table, to correct the sales person name for a specific sale.
    After the program is done interacting with the db, the program closes the connection.
"""

import sqlite3  # import the sqlite3 module, so we can interact with the DB in python

conn = sqlite3.connect('C:/Program Files/DB Browser for SQLite/SQL_Lab.db')   # connect to SQL_LAB.db

cursor = conn.cursor()  # create a cursor object so we can execute SQL statements

'''
    First drop existing tables if they exist to prevent conflict when inserting later. Afterwards, we will define
    a list of SQL tables called Customers, Orders, Products, and Sales, and 
    the SQL statements to create them if they do not exist.
'''

sqlTables = [
    'DROP TABLE IF EXISTS Customers;',
    'DROP TABLE IF EXISTS Orders;',
    'DROP TABLE IF EXISTS Products;',
    'DROP TABLE IF EXISTS Sales;',
    ''' CREATE TABLE IF NOT EXISTS Customers
    (customer_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    customer_age INTEGER
    ); ''',
    ''' CREATE TABLE IF NOT EXISTS Orders
    (order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    shipment_id INTEGER,
    quantity INTEGER
    ); ''',
    ''' CREATE TABLE IF NOT EXISTS Products
    (product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    product_category TEXT
    );  ''',
    ''' CREATE TABLE IF NOT EXISTS Sales
    (sales_id INTEGER,
    sales_person_name TEXT,
    product_id INTEGER,
    sales_amount INTEGER,
    PRIMARY KEY(sales_id, sales_person_name)
    ); '''
]

'''
    Execute each create statement, creating the tables in the DB.
'''

for table in sqlTables:
    cursor.execute(table)

'''
    Define a list of insert statements to insert test data into the DB for each of the existing tables.
'''

insertStatements = [
    ''' INSERT INTO Customers
        VALUES
        (100, 'John Svendson', 35),
        (200, 'Stephen Adams', 25),
        (300, 'Kari Pettersen', 40),
        (400, 'James McClure', 30); ''',
    ''' INSERT INTO Orders
        VALUES
        (1000, 100, 5000, 100),
        (1001, 400, 5050, 30),
        (1002, 100, 5100, 20),
        (1003, 200, 5500, 50),
        (1004, 200, 5350, 10),
        (1005, 300, 5450, 200); ''',
    ''' INSERT INTO Products
        VALUES
        (12, 'Bike ABC', 'Road Bike'),
        (13, 'Bike DEF', 'Mountain Bike'),
        (14, 'Bike GHI', 'Road Bike'),
        (15, 'BIKE JKL', 'Touring Bike'); ''',
    ''' INSERT INTO Sales
        VALUES
        (10000, 'Joe Brown', 12, 1000),
        (10001, 'Bill Johnson', 12, 5000),
        (10002, 'Joe Brown', 13, 10000),
        (10003, 'Bill Johnson', 15, 3000); '''
]

'''
    Execute each of the defined insert statements to insert the data into the DB.
'''

for insert in insertStatements:
    cursor.execute(insert)


'''
    Define a list of search statements containing the data we want to retrieve from the DB.
'''

selectStatements = [
    '''
        SELECT *
        FROM Customers
        WHERE customer_age > 30;
    ''',
    '''
        SELECT Customers.customer_name, Orders.order_id, Orders.quantity
        FROM Customers, Orders
        WHERE Customers.customer_id = Orders.customer_id
    ''',
    '''
        SELECT DISTINCT product_category
        FROM Products
    ''',
    '''
        SELECT Sales.sales_person_name, Sales.sales_amount, Products.product_name
        From   Sales, Products
        Where  Sales.product_id = Products.product_id AND Products.product_id = 12;'''
]

'''
    Execute the defined select statements using the cursor's execute method, and print the fetched results 
    using a for loop and the cursor's fetchall method.
'''

for i, select in enumerate(selectStatements):
    cursor.execute(select)
    results = cursor.fetchall()
    question = i + 4
    print(f"\nQ{question}")
    print("------------------------------------")
    for row in results:
        print(row)
    print("------------------------------------")

'''
    Define an update statement to correct the sales person name of a specific sale.
'''

updateStatement = '''
                Update Sales
                SET sales_person_name = 'Sophie Thomas'
                Where  Sales.sales_id = 10000'''


cursor.execute(updateStatement)     # Execute the defined update statement, updating the DB
conn.commit()   # Permanently commit the changes to the db
conn.close()    # Clean up resources, closing the connection to the db and the cursor
