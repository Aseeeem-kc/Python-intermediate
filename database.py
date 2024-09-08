"""
Database programming in Python involves using Python to interact with databases. This typically includes performing operations like querying, updating, and managing data stored in a database. Python provides various libraries and modules to work with different types of databases.

# Corresponding Python Libraries for different DBMS
SQLite: sqlite3
MySQL: mysql-connector-python
PostgreSQL: psycopg2
MongoDB: pymongo
"""

import sqlite3

class Person:
    
    def __init__(self, id_number=-1, first="", last="", age=-1):
        """
        Initializes a new Person instance and connects to the SQLite database.
        
        Parameters:
        id_number (int): Unique ID for the person.
        first (str): First name of the person.
        last (str): Last name of the person.
        age (int): Age of the person.
        """
        self.id_number = id_number
        self.first = first
        self.last = last
        self.age = age
        # Connect to the SQLite database file
        self.connection = sqlite3.connect('mydata.db')
        self.cursor = self.connection.cursor()

    def load_person(self, id_number):
        """
        Loads and updates the Person object with data from the database.
        
        Parameters:
        id_number (int): ID of the person to retrieve.
        """
        # Select person data using their ID
        self.cursor.execute("SELECT * FROM persons WHERE id = ?", (id_number,))
        results = self.cursor.fetchone()
        
        # Update object attributes with the retrieved data
        if results:
            self.id_number = id_number
            self.first = results[1]
            self.last = results[2]
            self.age = results[3]

    def insert_person(self):
        """
        Inserts the current Person instance into the database.
        """
        # Insert person data into the 'persons' table
        self.cursor.execute("INSERT INTO persons VALUES (?, ?, ?, ?)",
                            (self.id_number, self.first, self.last, self.age))
        self.connection.commit()  # Commit the transaction
        self.connection.close()   # Close the connection

# Example usage:

# Create a new Person instance and insert into the database
p1 = Person(7, "Alex", "Robins", 30)
p1.insert_person()

# Fetch and print all records from the 'persons' table
connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()
cursor.execute("SELECT * FROM persons")
results = cursor.fetchall()
print(results)
connection.close()

"""
Notes:
1. **SQLite**: A lightweight, file-based database system used here for simplicity.
2. **Database Connection**: Use `sqlite3.connect('filename.db')` to connect.
3. **Cursor**: Allows SQL commands to be executed (`cursor.execute()`).
4. **Parameterized Queries**: Use placeholders (`?`) to prevent SQL injection and handle data safely.
5. **Commit and Close**: Always commit changes with `connection.commit()` and close the connection with `connection.close()`.
"""
