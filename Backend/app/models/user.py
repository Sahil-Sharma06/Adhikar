from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from bson import ObjectId

# Helper to convert MongoDB's ObjectId into a str
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid object id")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


# Pydantic model for creating a new user
class UserCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)
    language_preference: Optional[str] = Field("en", description="User's language preference (e.g., en, fr)")

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "johndoe@example.com",
                "password": "strongpassword123",
                "language_preference": "en",
            }
        }


# Pydantic model for updating an existing user
class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr]
    password: Optional[str] = Field(None, min_length=6)
    language_preference: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "John Updated",
                "email": "newemail@example.com",
                "password": "newpassword",
                "language_preference": "fr",
            }
        }


# Pydantic model for user data stored in MongoDB (the response model)
class UserInDB(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    email: EmailStr
    hashed_password: str
    language_preference: Optional[str] = "en"

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "id": "60b6c5fe7c2a9c7d36ed7f23",
                "name": "John Doe",
                "email": "johndoe@example.com",
                "hashed_password": "hashedpassword123",
                "language_preference": "en",
            }
        }


# Pydantic model for returning user data in response (without the hashed password)
class UserOut(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    email: EmailStr
    language_preference: Optional[str] = "en"

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "id": "60b6c5fe7c2a9c7d36ed7f23",
                "name": "John Doe",
                "email": "johndoe@example.com",
                "language_preference": "en",
            }
        }
