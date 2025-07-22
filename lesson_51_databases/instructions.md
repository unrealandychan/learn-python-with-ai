# Lesson 51: Working with Databases (SQLAlchemy with SQLite)

SQLAlchemy is a powerful SQL toolkit and Object Relational Mapper (ORM) for Python. It provides a full suite of well-known enterprise-level persistence patterns, designed for efficient and high-performing database access.

We will use SQLite, a file-based database, which is excellent for learning and prototyping as it doesn't require a separate server. It stores the entire database in a single file.

## Key Concepts in SQLAlchemy

*   **Engine:** The starting point for any SQLAlchemy application. It's a factory for connections to a specific database. You create it using `create_engine()`.
*   **Declarative Base:** A base class that maintains a catalog of classes and tables relative to that base. Your Python classes that represent database tables will inherit from this base.
*   **Session:** The primary way to interact with the database. It manages the persistence of objects (your Python class instances) and provides methods for querying, adding, updating, and deleting data. It acts as a staging area for changes.
*   **Model (Table Definition):** A Python class that maps to a database table. Each attribute of the class typically maps to a column in the table.

## Installation

First, install SQLAlchemy:

```bash
pip install sqlalchemy
```

## Basic CRUD Operations with SQLAlchemy

Let's walk through the fundamental Create, Read, Update, and Delete (CRUD) operations.

### 1. Setup Database and Define Model

```python
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

# Define the database URL. For SQLite, it's 'sqlite:///./your_database_name.db'
# The './' means the database file will be created in the current directory.
DATABASE_URL = "sqlite:///./example.db"

# Create the SQLAlchemy engine. This is the entry point to the database.
engine = create_engine(DATABASE_URL)

# Create a declarative base. All your ORM models will inherit from this.
Base = declarative_base()

# Define your database model (Python class representing a table)
class User(Base):
    __tablename__ = "users" # Name of the table in the database

    id = Column(Integer, primary_key=True, index=True) # Primary key, auto-increments
    name = Column(String, index=True, nullable=False) # String column, cannot be null
    email = Column(String, unique=True, index=True, nullable=False) # Unique email
    age = Column(Integer, nullable=True) # Optional integer column

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"

# Create all defined tables in the database. This will create the 'users' table.
# If the table already exists, it will not be re-created.
Base.metadata.create_all(bind=engine)

# Create a SessionLocal class. Each instance of SessionLocal will be a database session.
# autocommit=False: We will manually commit transactions.
# autoflush=False: Changes are not flushed to the DB until commit or query.
# bind=engine: Binds the session to our database engine.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Helper function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

```

### 2. Create (Add Data)

To add new records, create instances of your model class, add them to the session, and then commit the session.

```python
# Example of adding data
with get_db() as db:
    # Create new User objects
    user1 = User(name="Alice", email="alice@example.com", age=30)
    user2 = User(name="Bob", email="bob@example.com", age=24)
    user3 = User(name="Charlie", email="charlie@example.com", age=35)

    # Add them to the session
    db.add(user1)
    db.add(user2)
    db.add(user3)

    # Commit the transaction to save changes to the database
    db.commit()

    # Refresh the objects to get their database-generated IDs (e.g., primary key)
    db.refresh(user1)
    db.refresh(user2)
    db.refresh(user3)

    print(f"Added users: {user1.name}, {user2.name}, {user3.name}")
```

### 3. Read (Query Data)

Querying is done using the session's `query()` method, followed by filtering and execution methods.

```python
from sqlalchemy import select # For modern SQLAlchemy 2.0 style queries

# Example of reading data
with get_db() as db:
    # Get all users
    all_users = db.query(User).all()
    print("\nAll Users:")
    for user in all_users:
        print(f"  ID: {user.id}, Name: {user.name}, Email: {user.email}, Age: {user.age}")

    # Get a user by ID
    user_by_id = db.query(User).filter(User.id == 1).first()
    if user_by_id:
        print(f"\nUser with ID 1: {user_by_id.name}")

    # Get users by name (case-sensitive)
    users_by_name = db.query(User).filter(User.name == "Alice").all()
    print("\nUsers named Alice:")
    for user in users_by_name:
        print(f"  {user.name} ({user.email})")

    # Get users with age greater than 30
    users_older_than_30 = db.query(User).filter(User.age > 30).all()
    print("\nUsers older than 30:")
    for user in users_older_than_30:
        print(f"  {user.name} (Age: {user.age})")

    # Using select() for modern SQLAlchemy 2.0 style (recommended for new code)
    # This requires importing `select` from `sqlalchemy`
    stmt = select(User).where(User.email == "bob@example.com")
    bob = db.scalar(stmt) # scalar() returns a single result or None
    if bob:
        print(f"\nFound Bob using select(): {bob.name}")

```

### 4. Update (Modify Data)

To update a record, first query it, modify its attributes, and then commit the session.

```python
# Example of updating data
with get_db() as db:
    user_to_update = db.query(User).filter(User.email == "alice@example.com").first()
    if user_to_update:
        user_to_update.age = 31 # Modify the attribute
        user_to_update.name = "Alicia" # Another modification
        db.commit() # Commit the changes
        db.refresh(user_to_update) # Refresh to get latest state from DB
        print(f"\nUpdated Alice: {user_to_update.name}, Age: {user_to_update.age}")

    # Verify the update
    updated_alice = db.query(User).filter(User.email == "alice@example.com").first()
    if updated_alice:
        print(f"  Verified updated Alice: {updated_alice.name}, Age: {updated_alice.age}")
```

### 5. Delete (Remove Data)

To delete a record, query it, use `session.delete()`, and then commit the session.

```python
# Example of deleting data
with get_db() as db:
    user_to_delete = db.query(User).filter(User.name == "Bob").first()
    if user_to_delete:
        db.delete(user_to_delete) # Mark for deletion
        db.commit() # Execute deletion
        print(f"\nDeleted user: {user_to_delete.name}")

    # Verify deletion
    remaining_users = db.query(User).all()
    print("\nUsers after deletion:")
    if remaining_users:
        for user in remaining_users:
            print(f"  {user.name}")
    else:
        print("  No users remaining.")
```

## Important Considerations

*   **Sessions:** Always ensure you close your database sessions (`db.close()`) to release resources. The `with get_db() as db:` pattern handles this automatically.
*   **Transactions:** `db.commit()` saves your changes. If an error occurs before `commit()`, you can use `db.rollback()` to undo changes.
*   **Error Handling:** Wrap database operations in `try...except` blocks to handle potential database errors (e.g., unique constraint violations).
*   **Migrations:** For managing changes to your database schema over time (e.g., adding new columns, altering tables), tools like Alembic are used in conjunction with SQLAlchemy.

This lesson provides a solid foundation for interacting with databases using SQLAlchemy. The ORM approach allows you to work with Python objects, abstracting away much of the raw SQL.