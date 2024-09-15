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

async def update_user_details(db, email: str, new_name: str = None, new_password: str = None, new_language: str = None):
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if new_name:
        user.name = new_name

    if new_password:
        if not verify_password(new_password, user.password):
            user.password = hash_password(new_password)
        else:
            raise HTTPException(status_code=400, detail="Current password is incorrect")

    if new_language:
        user.language_preference = new_language

    db.add(user)
    await db.commit()
    await db.refresh(user)
    
    return user