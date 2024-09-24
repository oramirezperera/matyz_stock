import sqlite3

conn = sqlite3.connect('tatoo_supplies.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS supplies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    quantity INTEGER NOT NULL,
    price_per_unit REAL NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    supply_id INTEGER,
    quantity_sold INTEGER,
    sale_date DATE DEFAULT (DATE('now')),
    FOREIGN KEY (supply_id) REFERENCES supplies (id)
);
''')

conn.commit()
conn.close()

print("Test Database an Tables created successfully")