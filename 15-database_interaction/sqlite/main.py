# Database Interaction with SQLite
# SQLite is a popular open-source relational database management system. 
# It is a self-contained, serverless, zero-configuration, transactional SQL database engine.

# Import the sqlite3 module. It is by default installed with Python
import sqlite3
import os

# Function to create the users table
def create_table(conn):
    # Create a cursor object
    cur = conn.cursor()
    
    # Create table if it doesn't exist
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

# Function to insert records into the users table
def insert_records(conn):
    # Create a cursor object
    cur = conn.cursor()
    
    # Insert records
    cur.execute("INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com')")
    cur.execute("INSERT INTO users (name, email) VALUES ('Jane Doe', 'jane@example.com')")
    cur.execute("INSERT INTO users (name, email) VALUES ('Bob Smith', 'bob@example.com')")
    cur.execute("INSERT INTO users (name, email) VALUES ('Alice Smith', 'alice@example.com')")
    cur.execute("INSERT INTO users (name, email) VALUES ('Eve Smith', 'eve@example.com')")
    cur.execute("INSERT INTO users (name, email) VALUES ('Charlie Smith', 'charlie@example.com')")
    cur.execute("INSERT INTO users (name, email) VALUES ('David Baker', 'david@example.com')")
    cur.execute("INSERT INTO users (name, email) VALUES ('Frank Baker', 'frank@example.com')")
    cur.execute("INSERT INTO users (name, email) VALUES ('George Gray', 'george@example.com')")
    cur.execute("INSERT INTO users (name, email) VALUES ('Harry Gray', 'harry@example.com')")

    # Commit changes
    conn.commit()

# Function to retrieve records from the users table
def retrieve_records(conn):
    # Create a cursor object
    cur = conn.cursor()
    
    # Retrieve records
    cur.execute("SELECT * FROM users")
    
    # Fetch all records
    rows = cur.fetchall()
    
    # Print records
    for row in rows:
        print(row)

# Function to update a record in the users table
def update_record(conn):
    # Create a cursor object
    cur = conn.cursor()
    
    # Update record
    cur.execute("UPDATE users SET name = 'Bob Baker' WHERE id = 3")
    
    # Commit changes
    conn.commit()

# Function to delete a record from the users table
def delete_record(conn):
    # Create a cursor object
    cur = conn.cursor()
    
    # Delete record
    cur.execute("DELETE FROM users WHERE id = 2")
    
    # Commit changes
    conn.commit()

# Main function
def main():
    # Get the path of the current script
    script_path = os.path.dirname(__file__)

    # Construct the path to the SQLite database file
    db_path = os.path.join(script_path, 'my_sqlite.db')

    # Check if the database file exists, if not create it. Finally open and connect to SQLite database locate at the sqlite folder
    conn = sqlite3.connect(db_path)
    
    # Create the users table
    create_table(conn)
    
    # Insert records into the users table
    insert_records(conn)
    
    # Retrieve records from the users table
    print("Records before update:")
    retrieve_records(conn)
    
    # Update a record in the users table
    update_record(conn)
    
    # Retrieve records from the users table
    print("Records after update:")
    retrieve_records(conn)
    
    # Delete a record from the users table
    delete_record(conn)
    
    # Retrieve records from the users table
    print("Records after delete:")
    retrieve_records(conn)
    
    # Close the connection
    conn.close()

# Run the main function
# __name__ is a special variable in Python that holds the name of the current module
# __main__ is the name of the main module

if __name__ == '__main__':
    main()

# Output:
# Records before update:
# (1, 'John Doe', 'john@example.com')
# (2, 'Jane Doe', 'jane@example.com')
# (3, 'Bob Smith', 'bob@example.com')
# (4, 'Alice Smith', 'alice@example.com')
# (5, 'Eve Smith', 'eve@example.com')
# (6, 'Charlie Smith', 'charlie@example.com')
# (7, 'David Baker', 'david@example.com')
# (8, 'Frank Baker', 'frank@example.com')
# (9, 'George Gray', 'george@example.com')
# (10, 'Harry Gray', 'harry@example.com')
# Records after update:
# (1, 'John Doe', 'john@example.com')
# (2, 'Jane Doe', 'jane@example.com')
# (3, 'Bob Baker', 'bob@example.com')
# (4, 'Alice Smith', 'alice@example.com')
# (5, 'Eve Smith', 'eve@example.com')
# (6, 'Charlie Smith', 'charlie@example.com')
# (7, 'David Baker', 'david@example.com')
# (8, 'Frank Baker', 'frank@example.com')
# (9, 'George Gray', 'george@example.com')
# (10, 'Harry Gray', 'harry@example.com')
# Records after delete:
# (1, 'John Doe', 'john@example.com')
# (3, 'Bob Baker', 'bob@example.com')
# (4, 'Alice Smith', 'alice@example.com')
# (5, 'Eve Smith', 'eve@example.com')
# (6, 'Charlie Smith', 'charlie@example.com')
# (7, 'David Baker', 'david@example.com')
# (8, 'Frank Baker', 'frank@example.com')
# (9, 'George Gray', 'george@example.com')
# (10, 'Harry Gray', 'harry@example.com')