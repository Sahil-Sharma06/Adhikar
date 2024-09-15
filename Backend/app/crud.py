from sqlalchemy.future import select
from .models import User

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