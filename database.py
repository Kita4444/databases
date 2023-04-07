import math
import sqlite3


connect = sqlite3.connect('customer.db')

cursor = connect.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS customers (
                first_name text,
                last_name text,
                gmail text               
               )""")

cursor.execute("SELECT * FROM customers")

print(cursor.fetchall())


many_customers = [
                  ('Wes', 'Brown', 'brown@gmail.com'), 
                  ('Con', 'Lon', 'con@gmail.com'), 
                  ('Gam', 'Mag', 'gam@gmail.com')
                 ]

cursor.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)
               
print ("Command executed succesfully...")

connect.commit()

connect.close()




