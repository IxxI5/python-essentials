# Database Interaction with SQLAlchemy
# SQLAlchemy is an object-relational mapper (ORM) for Python for working with databases.
# SQLAlchemy maps your databases (tables, etc.) to Python objects, so that you can more easily and natively interact with them.
# SQLAlchemy can be used with sqlite, MySQL, PostgreSQL, etc.

# Install sqlalchemy (before using it) via terminal: pip install sqlalchemy

# Import the necessary modules
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Get the path of the current script
script_path = os.path.dirname(__file__)

# Construct the path to the SQLAlchemy database file
db_path = os.path.join(script_path, 'my_sqlalchemy.db')

# Create a connection to the SQLite database located at the sqlalchemy folder
engine = create_engine(f'sqlite:///{db_path}')

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define a class that inherits from Base and represents our table.  
class User(Base):
    # Define the table name
    __tablename__ = 'users'
    # Define the columns
    id = Column(Integer, primary_key=True)
    username = Column(String)
    location = Column(String)

    def __repr__(self):
        """Return a string representation of the User object."""
        return f"User(id={self.id}, username='{self.username}', location='{self.location}')"

# Create all tables in the engine
Base.metadata.create_all(engine)

# Create a session
session = Session()

# Insert records into the users table
new_user1 = User(username='JohnDoe', location='New York')
new_user2 = User(username='JaneDoe', location='Los Angeles')
new_user3 = User(username='BobSmith', location='Chicago')
new_user4 = User(username='AliceJohnson', location='Houston')
new_user5 = User(username='CharlieBrown', location='Philadelphia')
new_user6 = User(username='EveSmith', location='San Francisco')
new_user7 = User(username='FrankJohnson', location='Seattle')
new_user8 = User(username='GraceSmith', location='Denver')

session.add(new_user1)
session.add(new_user2)
session.add(new_user3)
session.add(new_user4)
session.add(new_user5)
session.add(new_user6)
session.add(new_user7)
session.add(new_user8)

# Commit the changes
session.commit()

# Retrieve records from the users table
users = session.query(User).all()

print("Initial records:")
for user in users:
    print(user)

# Update a record in the users table
user_to_update = session.query(User).filter_by(username='JohnDoe').first()
user_to_update.location = 'San Francisco'

session.commit()

# Retrieve records from the users table
users = session.query(User).all()
print("Updated records:")
for user in users:
    print(user)

# Delete a record from the users table
user_to_delete = session.query(User).filter_by(username='JaneDoe').first()
session.delete(user_to_delete)

session.commit()

# Retrieve records from the users table
users = session.query(User).all()
print("Records after deletion:")
for user in users:
    print(user)

# Close the session
session.close()

# Close the engine
engine.dispose()

# Output:
# Initial records:
# User(id=1, username='JohnDoe', location='New York')
# User(id=2, username='JaneDoe', location='Los Angeles')
# User(id=3, username='BobSmith', location='Chicago')
# User(id=4, username='AliceJohnson', location='Houston')
# User(id=5, username='CharlieBrown', location='Philadelphia')
# User(id=6, username='EveSmith', location='San Francisco')
# User(id=7, username='FrankJohnson', location='Seattle')
# User(id=8, username='GraceSmith', location='Denver')
# Updated records:
# User(id=1, username='JohnDoe', location='San Francisco')
# User(id=2, username='JaneDoe', location='Los Angeles')
# User(id=3, username='BobSmith', location='Chicago')
# User(id=4, username='AliceJohnson', location='Houston')
# User(id=5, username='CharlieBrown', location='Philadelphia')
# User(id=6, username='EveSmith', location='San Francisco')
# User(id=7, username='FrankJohnson', location='Seattle')
# User(id=8, username='GraceSmith', location='Denver')
# Records after deletion:
# User(id=1, username='JohnDoe', location='San Francisco')
# User(id=3, username='BobSmith', location='Chicago')
# User(id=4, username='AliceJohnson', location='Houston')
# User(id=5, username='CharlieBrown', location='Philadelphia')
# User(id=6, username='EveSmith', location='San Francisco')
# User(id=7, username='FrankJohnson', location='Seattle')
# User(id=8, username='GraceSmith', location='Denver')