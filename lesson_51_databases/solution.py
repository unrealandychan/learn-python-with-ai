

# Lesson 51: Solution

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Setup Database
DATABASE_URL = "sqlite:///./products.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# 2. Define Table (Model)
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price})>"

# 3. Create Tables
Base.metadata.create_all(bind=engine)

# 4. Create Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

# 5. Add Products
product1 = Product(name="Laptop", price=1200.00)
product2 = Product(name="Mouse", price=25.50)
product3 = Product(name="Keyboard", price=75.00)

db.add_all([product1, product2, product3])
db.commit()
print("Added products.")

# 6. Query All Products
print("\nAll Products:")
products = db.query(Product).all()
for p in products:
    print(p)

# 7. Update a Product
product_to_update = db.query(Product).filter(Product.name == "Laptop").first()
if product_to_update:
    product_to_update.price = 1150.00
    db.commit()
    db.refresh(product_to_update)
    print(f"\nUpdated Laptop price to: {product_to_update.price}")

# 8. Delete a Product
product_to_delete = db.query(Product).filter(Product.name == "Mouse").first()
if product_to_delete:
    db.delete(product_to_delete)
    db.commit()
    print("\nDeleted Mouse.")

# 9. Query All Products Again
print("\nProducts after update and delete:")
products = db.query(Product).all()
for p in products:
    print(p)

db.close()

