from fastapi import FastAPI, Depends
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .database import engine, get_db
from .crud import get_users, create_user, authenticate_user, create_access_token
from .models import Base

app = FastAPI()

# Create database tables automatically
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/users/")
async def read_users(db: AsyncSession = Depends(get_db)):
    users = await get_users(db)
    return users

@app.post("/signup/")
async def create_new_user(name: str, email: str, password: str, language_preference: str = "English", db: AsyncSession = Depends(get_db)):
    user = await create_user(db, name, email, password, language_preference)
    return user

@app.post("/login/")
async def login(email: str, password: str, db: AsyncSession = Depends(get_db)):
    user = await authenticate_user(db, email, password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Create JWT token upon successful authentication
    access_token = create_access_token(data={"sub": user.email})
    
    return {"access_token": access_token, "token_type": "bearer"}