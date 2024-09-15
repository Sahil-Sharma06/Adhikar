from motor.motor_asyncio import AsyncIOMotorDatabase
from app.models.user import UserCreate, UserUpdate, UserInDB
from bson import ObjectId
from typing import Optional


# Create a new user in the MongoDB database
async def create_user(db: AsyncIOMotorDatabase, user: UserCreate, hashed_password: str) -> UserInDB:
    user_doc = {
        "name": user.name,
        "email": user.email,
        "hashed_password": hashed_password,
        "language_preference": user.language_preference
    }
    
    result = await db["users"].insert_one(user_doc)
    user_in_db = UserInDB(**user_doc, id=result.inserted_id)
    return user_in_db


# Retrieve a user from the database by email
async def get_user_by_email(db: AsyncIOMotorDatabase, email: str) -> Optional[UserInDB]:
    user_doc = await db["users"].find_one({"email": email})
    if user_doc:
        return UserInDB(**user_doc)
    return None


# Retrieve a user from the database by user ID
async def get_user_by_id(db: AsyncIOMotorDatabase, user_id: str) -> Optional[UserInDB]:
    user_doc = await db["users"].find_one({"_id": ObjectId(user_id)})
    if user_doc:
        return UserInDB(**user_doc)
    return None


# Update user details in the database
async def update_user(db: AsyncIOMotorDatabase, user_id: str, user_update: UserUpdate) -> Optional[UserInDB]:
    update_data = {k: v for k, v in user_update.dict(exclude_unset=True).items()}
    
    if "password" in update_data:
        # If password is being updated, it should be hashed (hashing logic should be implemented elsewhere)
        update_data["hashed_password"] = update_data.pop("password")

    result = await db["users"].update_one(
        {"_id": ObjectId(user_id)},
        {"$set": update_data}
    )
    
    if result.matched_count == 1:
        updated_user = await get_user_by_id(db, user_id)
        return updated_user
    return None


# Delete a user by user ID
async def delete_user(db: AsyncIOMotorDatabase, user_id: str) -> bool:
    result = await db["users"].delete_one({"_id": ObjectId(user_id)})
    return result.deleted_count == 1
