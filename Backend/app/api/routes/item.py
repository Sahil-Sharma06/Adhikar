# app/api/routes/item.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/items/")
async def get_items():
    return [{"item_id": "1", "name": "Item One"}, {"item_id": "2", "name": "Item Two"}]
