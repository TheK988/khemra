from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate, UserOut
from crud import create_user, get_user, list_users
from database import get_db

app = FastAPI()

@app.post("/users", response_model=UserOut)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

@app.get("/users/{user_id}", response_model=UserOut)
def get_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    return get_user(db=db, user_id=user_id)

@app.get("/users", response_model=list[UserOut])
def list_users_endpoint(db: Session = Depends(get_db)):
    return list_users(db=db)
