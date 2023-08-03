import sqlite3

con = sqlite3.connect("database.db")

print("db opened")



con.execute("CREATE TABLE students (name TEXT , phoneNumber TEXT)")

print("table created")
con.close()