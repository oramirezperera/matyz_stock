''' Creating a file to create the DB '''
#importing libraries
import sqlite3

#connecting the Database
conn = sqlite3.connect('supplies.db')
cursor = conn.cursor()

# Creating the supplies table
cursor.execute('''
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    QUANTITY INTEGER NOT NULL,
    price_per_unit REAL NOT NULL,
    category TEXT NOT NULL,
    brand TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS customers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT,
    phone TEXT,
    tattoo_tag TEXT,
    ig_account TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS sales(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    quantity_sold INTEGER NOT NULL,
    sale_date DATE DEFAULT (DATE('now')),
    customer_id INTEGER,
    FOREIGN KEY (product_id) REFERENCES products (id)
    FOREIGN KEY (customer_id) REFERENCES customers (id)
);
'''
)

# Commit Changes and close
conn.commit()
conn.close()

print("Database and tables created successfully")