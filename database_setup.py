''' Creating a file to create the DB '''
#importing libraries
import sqlite3

#connecting the Database
conn = sqlite3.connect('supplies.db')
cursor = conn.cursor()

# Creating the supplies table
cursor.execute('''
CREATE TABLE IF NOT EXISTS supplies(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    QUANTITY INTEGER NOT NULL,
    price_per_unit REAL NOT NULL
);
''')