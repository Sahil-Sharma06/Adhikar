from fastapi import APIRouter, Depends
from app.models.user import UserCreate, UserInDB
from app.crud.user_crud import create_user, get_user_by_email

router = APIRouter()

@router.post("/register", response_model=UserInDB)
async def register_user(user: UserCreate):
    db_user = await get_user_by_email(user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await create_user(user)
