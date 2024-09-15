from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.utils import hash_password, verify_password
from app.crud import update_user_details

router = APIRouter()

@router.put("/change-name/")
async def change_name(new_name: str, email: str, db: AsyncSession = Depends(get_db)):
    user = await update_user_details(db, email=email, new_name=new_name)
    if not user:
        raise HTTPException(status_code=400, detail="Failed to update name")
    return {"message": "Name updated successfully"}

@router.put("/change-password/")
async def change_password(email: str, current_password: str, new_password: str, db: AsyncSession = Depends(get_db)):
    user = await update_user_details(db, email=email, current_password=current_password, new_password=new_password)
    if not user:
        raise HTTPException(status_code=400, detail="Failed to update password")
    return {"message": "Password updated successfully"}

@router.put("/change-language/")
async def change_language(email: str, new_language: str, db: AsyncSession = Depends(get_db)):
    user = await update_user_details(db, email=email, new_language=new_language)
    if not user:
        raise HTTPException(status_code=400, detail="Failed to update language")
    return {"message": "Language updated successfully"}
