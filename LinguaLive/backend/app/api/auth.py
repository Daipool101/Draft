from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import User

router = APIRouter()

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(SessionLocal)):
    # Dummy auth for MVP
    user = db.query(User).filter(User.username == username).first()
    if not user or user.hashed_password != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "user_id": user.id}

@router.post("/register")
def register(username: str, password: str, db: Session = Depends(SessionLocal)):
    user = User(username=username, hashed_password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "User registered", "user_id": user.id}