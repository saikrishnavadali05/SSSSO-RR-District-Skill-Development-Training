import sqlite3

# Create an in-memory SQLite database
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create a sample table
cursor.execute("CREATE TABLE students (id INTEGER, name TEXT)")
cursor.execute("INSERT INTO students VALUES (1, 'Alice'), (2, 'Bob')")

# Execute SELECT query
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
#Output: 
# (1, 'Alice')
# (2, 'Bob')
