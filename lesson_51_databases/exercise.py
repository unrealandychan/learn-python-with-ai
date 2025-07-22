# Lesson 51: Working with Databases (SQLAlchemy with SQLite) - Exercise

## Objective
This exercise will guide you through defining a simple database model, performing basic Create, Read, Update, and Delete (CRUD) operations using SQLAlchemy with a SQLite database.

## Instructions

1.  **Setup:** Ensure you have SQLAlchemy installed (`pip install sqlalchemy`).
2.  **Run the script:** Execute this `exercise.py` file. It will create a SQLite database file named `products.db` in the same directory.
3.  **Observe the output:** Follow the print statements to see the results of each database operation.
4.  **Verify (Optional):** You can use a SQLite browser (like DB Browser for SQLite) to open `products.db` and visually inspect the table and data after running the script.

---

```python
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Setup Database
# Define the database URL for a SQLite database named 'products.db'
DATABASE_URL = "sqlite:///./products.db"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a declarative base for our models
Base = declarative_base()

# 2. Define the Product Model
# This class will map to a table named 'products' in our database
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True) # Primary key, auto-incrementing
    name = Column(String, unique=True, index=True, nullable=False) # Product name, must be unique
    price = Column(Float, nullable=False) # Product price

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price:.2f})>"

# Create all defined tables in the database (if they don't already exist)
Base.metadata.create_all(bind=engine)

# Create a SessionLocal class to get database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Helper function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- CRUD Operations ---

print("\n--- Starting CRUD Operations ---")

# CREATE: Add three new products
with get_db() as db:
    print("\nAdding new products...")
    product1 = Product(name="Laptop", price=1200.00)
    product2 = Product(name="Mouse", price=25.50)
    product3 = Product(name="Keyboard", price=75.00)

    db.add_all([product1, product2, product3])
    db.commit()

    # Refresh to get IDs assigned by the database
    db.refresh(product1)
    db.refresh(product2)
    db.refresh(product3)

    print(f"Added: {product1.name}, {product2.name}, {product3.name}")

# READ: Query and print all products
with get_db() as db:
    print("\nAll products in the database:")
    all_products = db.query(Product).all()
    if all_products:
        for product in all_products:
            print(f"  {product}")
    else:
        print("  No products found.")

# UPDATE: Update the price of one product (e.g., Laptop)
with get_db() as db:
    print("\nUpdating Laptop price...")
    laptop = db.query(Product).filter(Product.name == "Laptop").first()
    if laptop:
        old_price = laptop.price
        laptop.price = 1150.00 # New price
        db.commit()
        db.refresh(laptop)
        print(f"Updated {laptop.name} from ${old_price:.2f} to ${laptop.price:.2f}")
    else:
        print("Laptop not found for update.")

# DELETE: Delete one product (e.g., Mouse)
with get_db() as db:
    print("\nDeleting Mouse...")
    mouse = db.query(Product).filter(Product.name == "Mouse").first()
    if mouse:
        db.delete(mouse)
        db.commit()
        print(f"Deleted: {mouse.name}")
    else:
        print("Mouse not found for deletion.")

# READ: Query and print all products again to verify changes
with get_db() as db:
    print("\nAll products after update and delete operations:")
    remaining_products = db.query(Product).all()
    if remaining_products:
        for product in remaining_products:
            print(f"  {product}")
    else:
        print("  No products remaining.")

print("\n--- CRUD Operations Complete ---")
```