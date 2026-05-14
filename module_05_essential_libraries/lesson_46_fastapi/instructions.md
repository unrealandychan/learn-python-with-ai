# Lesson 46: `FastAPI` - Building Web APIs

`FastAPI` is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints. It's designed to be easy to use, highly performant, and comes with automatic interactive API documentation.

**Key Features of FastAPI:**
*   **Fast**: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic).
*   **Fast to code**: Increase development speed by about 200% to 300%.
*   **Fewer bugs**: Reduce about 40% of human (developer) induced errors.
*   **Intuitive**: Great editor support with autocompletion everywhere.
*   **Easy**: Designed to be easy to use and learn.
*   **Short**: Minimize code duplication.
*   **Robust**: Get production-ready code with automatic interactive documentation.
*   **Standards-based**: Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously Swagger) and JSON Schema.

**Official Documentation:** [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)

---

### Installation

To use FastAPI, you need to install it along with an ASGI server, such as Uvicorn.

```bash
pip install fastapi "uvicorn[standard]"
```

### Basic API Structure

A FastAPI application typically starts by creating a `FastAPI` instance.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def read_root():
    return {"message": "Hello, World!"}

# To run this application, save it as main.py and run:
# uvicorn main:app --reload
```

### Running the Application

To run your FastAPI application, you use Uvicorn. If your file is named `main.py` and your FastAPI instance is named `app`:

```bash
uvicorn main:app --reload
```

*   `main`: refers to the `main.py` file.
*   `app`: refers to the `app` object inside `main.py`.
*   `--reload`: makes the server restart automatically when you make code changes.

Once running, you can access your API at `http://127.0.0.1:8000` (or whatever address Uvicorn specifies).

### Automatic Interactive API Documentation

FastAPI automatically generates interactive API documentation based on the OpenAPI standard. You can access it at:

*   **Swagger UI**: `http://127.0.0.1:8000/docs`
*   **ReDoc**: `http://127.0.0.1:8000/redoc`

These interfaces allow you to test your API endpoints directly from your browser.

### Path Operations

FastAPI uses *path operation decorators* to define how a specific URL path should be handled for different HTTP methods (GET, POST, PUT, DELETE, etc.).

#### GET Requests

Used to retrieve data.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str):
    return {"user_id": user_id, "item_id": item_id}
```

#### Path Parameters

Path parameters are defined using curly braces `{}` in the path. FastAPI automatically converts them to the specified type (e.g., `int`, `str`).

```python
# Example shown above: item_id: int
```

#### Query Parameters

Query parameters are defined as function parameters that are not part of the path. They are optional by default.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

# Access with: /items/?skip=5&limit=20
```

#### POST Requests and Request Body

Used to send data to the server to create or update a resource. FastAPI uses Pydantic models to define the structure and validation of the request body.

First, define a Pydantic model:

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
```

Then, use it in your path operation:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/items/")
async def create_item(item: Item):
    return item

# When you send a POST request to /items/ with a JSON body like:
# {"name": "Foo", "price": 10.5}
# FastAPI will validate the data and provide it as an Item object.
```

#### PUT Requests

Used to update an existing resource.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}
```

#### DELETE Requests

Used to delete a resource.

```python
from fastapi import FastAPI

app = FastAPI()

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted"}
```

---

### Quiz

1.  **What is the primary benefit of using Pydantic models in FastAPI?**
    a) To make the API slower.
    b) To provide data validation and serialization/deserialization.
    c) To connect to a database.

2.  **How do you run a FastAPI application (assuming the file is `main.py` and the app instance is `app`)?**
    a) `python main.py`
    b) `fastapi run app`
    c) `uvicorn main:app --reload`

3.  **Where can you find the automatic interactive API documentation for a running FastAPI app?**
    a) `/docs` or `/redoc`
    b) `/api-docs`
    c) You have to write it manually.

<details>
  <summary><b>Answer Key</b></summary>
  1. b
  2. c
  3. a
</details>