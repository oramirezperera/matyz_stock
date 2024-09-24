import sqlite3

conn = sqlite3.connect('tatoo_supplies.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM supplies")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
