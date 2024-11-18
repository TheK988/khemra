from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# Initialize the FastAPI app
app = FastAPI()

# Pydantic model for User data validation
class User(BaseModel):
    name: str
    age: int = Field(..., ge=18, description="Age must be 18 or older")
    email: EmailStr

# POST endpoint to create a new user
@app.post("/create_user/")
def create_user(user: User):
    # If the data passes validation, return a success message
    return {
        "message": "User created successfully!",
        "user": {
            "name": user.name,
            "age": user.age,
            "email": user.email
        }
    }
