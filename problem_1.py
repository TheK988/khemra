from fastapi import FastAPI

# Initialize the FastAPI app
app = FastAPI()

# Define a route for /hello/{name}
@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}

