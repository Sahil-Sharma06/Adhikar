from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from pydantic import BaseModel
import httpx

router = APIRouter()

class LawDetail(BaseModel):
    text: str

# POST API for /knowlaw
@router.post("/knowlaw")
async def know_law(detail: LawDetail, db: AsyncSession = Depends(get_db)):
    """
    Endpoint to fetch law details from the local API based on the provided text.
    """
    try:
        text_input = detail.text

        # Call the local API (http://localhost:8080/question/{text_input})
        async with httpx.AsyncClient() as client:
            response = await client.get(f"http://localhost:8080/question/{text_input}")

        # Check if the local API request was successful
        if response.status_code == 200:
            # Parse the response from the local API
            external_response = response.json()
            law_text = external_response.get("message")

            # Handle the case where the local API returns an invalid response
            if not law_text:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid response from local API")

            # Return the law details
            return {"Law": law_text}

        else:
            # Raise an exception if the local API returns an error
            raise HTTPException(status_code=response.status_code, detail="Error calling local API")

    except Exception as e:
        # Catch any unexpected errors and raise an HTTP exception
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"An error occurred: {str(e)}")