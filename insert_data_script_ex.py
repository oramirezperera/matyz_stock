# Import libraries
import sqlite3

#connection to the DB
conn = sqlite3.connect('tatoo_supplies.db')
cursor = conn.cursor()

# Inserting the data
supplies_data = [
    ('Black Ink', 'High Quality Black Ink', 50, 10.00),
    ('Needles', 'Standard Tattoo Needles', 100, 1.50),
    ('Gloves', 'Disposable gloves, Size M', 200, 0.10)
]

cursor.executemany('''
    INSERT INTO supplies (name, description, quantity, price_per_unit)
    VALUES (?,?,?,?)
''', supplies_data)

conn.commit()

conn.close()

print("Sample data inserted to tatoo_suplies.db in the table supplies")