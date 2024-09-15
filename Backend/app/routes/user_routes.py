from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import get_users, create_user, authenticate_user
from app.auth import create_access_token
from app.database import get_db

router = APIRouter()

@router.get("/users/")
async def read_users(db: AsyncSession = Depends(get_db)):
    users = await get_users(db)
    return users

@router.post("/signup/")
async def create_new_user(name: str, email: str, password: str, language_preference: str = "English", db: AsyncSession = Depends(get_db)):
    user = await create_user(db, name, email, password, language_preference)
    return {"user":user}

@router.post("/login/")
async def login(email: str, password: str, db: AsyncSession = Depends(get_db)):
    user = await authenticate_user(db, email, password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Create JWT token upon successful authentication
    access_token = create_access_token(data={"sub": user.email})
    
    return {"access_token": access_token, "token_type": "bearer", "user":user}
