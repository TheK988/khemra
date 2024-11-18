from fastapi import FastAPI
from typing import Optional

# Initialize the FastAPI app
app = FastAPI()

# Define a route for /hello/{name}, with an optional query parameter 'age'
@app.get("/hello/{name}")
def hello(name: str, age: Optional[int] = None):
    if age:
        return {"message": f"Hello, {name}! You are {age} years old."}
    return {"message": f"Hello, {name}!"}
