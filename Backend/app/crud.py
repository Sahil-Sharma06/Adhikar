from sqlalchemy.future import select
from fastapi import HTTPException
from app.models import User
from app.utils import hash_password, verify_password

async def get_users(db):
    result = await db.execute(select(User))
    return result.scalars().all()

async def create_user(db, name: str, email: str, password: str, language_preference: str):
    # Check if user already exists
    result = await db.execute(select(User).where(User.email == email))
    existing_user = result.scalar_one_or_none()
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(password)
    user = User(name=name, email=email, password=hashed_password, language_preference=language_preference)
    
    db.add(user)
    await db.commit()
    await db.refresh(user)
    
    return user

async def authenticate_user(db, email: str, password: str):
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()

    if not user or not verify_password(password, user.password):
        return None  # User not found or incorrect password

    return user
