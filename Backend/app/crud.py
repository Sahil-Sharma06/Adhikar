from sqlalchemy.future import select
from fastapi import HTTPException
from .models import User
from .utils import verify_password, create_access_token hash_password

async def get_users(db):
    result = await db.execute(select(User))
    return result.scalars().all()

async def create_user(db, name: str, email: str, password: str, language_preference: str):
    # Check if a user with the same email already exists
    result = await db.execute(select(User).where(User.email == email))
    existing_user = result.scalar_one_or_none()
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the password
    hashed_password = hash_password(password)
    user = User(name=name, email=email, password=hashed_password, language_preference=language_preference)
    
    db.add(user)
    await db.commit()
    await db.refresh(user)
    
    return user

async def authenticate_user(db, email: str, password: str):
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()

    if not user:
        return None  # User not found
    if not verify_password(password, user.password):
        return None  # Incorrect password

    return user 