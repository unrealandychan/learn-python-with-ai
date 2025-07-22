# Lesson 46: `FastAPI` - Building Web APIs

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

# Initialize FastAPI app
app = FastAPI(
    title="Simple Item API",
    description="A basic API for managing items."
)

# In-memory database for demonstration purposes
db: Dict[int, Dict] = {}
next_item_id = 1

# Pydantic model for Item (used for request body validation)
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

# Pydantic model for Item creation (ID is not required for creation)
class ItemCreate(BaseModel):
    name: str
    description: str | None = None
    price: float

# Pydantic model for Item update (all fields are optional for partial update)
class ItemUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None

# --- Exercise 1: Basic GET Endpoint ---
# Task: Create a GET endpoint at the root ("/") that returns a simple welcome message.
# Test it by navigating to http://127.0.0.1:8000/ in your browser after running the app.
@app.get('/')
async def read_root():
    return {"message": "Welcome to the Item API!"}

# --- Exercise 2: GET with Path Parameter ---
# Task: Create a GET endpoint to retrieve a single item by its ID.
# If the item is not found, return a 404 HTTP exception.
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    return db[item_id]

# --- Exercise 3: GET with Query Parameters ---
# Task: Create a GET endpoint to list all items, with optional `skip` and `limit` query parameters.
# `skip` should default to 0, `limit` should default to 10.
@app.get("/items/")
async def list_items(skip: int = 0, limit: int = 10):
    items_list = list(db.values())
    return items_list[skip : skip + limit]

# --- Exercise 4: POST Request with Pydantic Model ---
# Task: Create a POST endpoint to add a new item to the database.
# Use the `ItemCreate` Pydantic model for the request body.
# Assign a unique ID to the new item.
@app.post("/items/", status_code=201) # 201 Created status code
async def create_item(item: ItemCreate):
    global next_item_id
    item_data = item.model_dump() # Convert Pydantic model to dict
    db[next_item_id] = {"id": next_item_id, **item_data}
    next_item_id += 1
    return db[next_item_id - 1]

# --- Exercise 5: PUT Request to Update an Item ---
# Task: Create a PUT endpoint to update an existing item by its ID.
# Use the `ItemUpdate` Pydantic model for the request body.
# If the item is not found, return a 404 HTTP exception.
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: ItemUpdate):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    
    current_item_data = db[item_id]
    updated_data = item.model_dump(exclude_unset=True) # Only update provided fields
    current_item_data.update(updated_data)
    db[item_id] = current_item_data
    return db[item_id]

# --- Exercise 6: DELETE Request ---
# Task: Create a DELETE endpoint to remove an item by its ID.
# If the item is not found, return a 404 HTTP exception.
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    del db[item_id]
    return {"message": f"Item {item_id} deleted successfully"}

# Instructions to run:
# 1. Save this file as `main.py` (or any other name, e.g., `app.py`).
# 2. Open your terminal in the same directory as this file.
# 3. Run the command: `uvicorn main:app --reload`
# 4. Open your browser and go to `http://127.0.0.1:8000/docs` to see the interactive API documentation (Swagger UI).
# 5. Test the endpoints using the Swagger UI or a tool like Postman/Insomnia/curl.
