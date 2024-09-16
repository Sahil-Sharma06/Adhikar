from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import get_users, create_user, authenticate_user
from app.auth import create_access_token
from app.database import get_db
from pydantic import BaseModel, EmailStr

router = APIRouter()


class UserCreateRequest(BaseModel):
    name: str
    email: str
    password: str
    language_preference: str = "English"
    type: str="Client"


@router.get("/users/")
async def read_users(db: AsyncSession = Depends(get_db)):
    users = await get_users(db)
    return users

@router.post("/signup/")
async def create_new_user(user: UserCreateRequest, db: AsyncSession = Depends(get_db)):
    user_data = user.dict()
    name = user_data['name']
    email = user_data['email']
    password = user_data['password']
    language_preference = user_data['language_preference']
    
    user = await create_user(db, name, email, password, language_preference)
    return {"user": user}

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

@router.post("/login/")
async def login(login_data: LoginRequest, db: AsyncSession = Depends(get_db)):
    # Extract the email and password from the Pydantic model
    email = login_data.email
    password = login_data.password
    
    # Authenticate user
    user = await authenticate_user(db, email, password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Create JWT token upon successful authentication
    access_token = create_access_token(data={"sub": user.email})
    
    return {"access_token": access_token, "token_type": "bearer", "user": user}
