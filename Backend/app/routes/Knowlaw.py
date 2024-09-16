from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import get_users, create_user, authenticate_user
from app.auth import create_access_token
from app.database import get_db
import os
from pydantic import BaseModel
import httpx

router = APIRouter()

class LawDetail(BaseModel):
    text: str

# Function to fetch details from Gemini API
async def fetch_law_details_from_gemini(law_name: str, api_key: str) -> dict:
    """
    Fetch details about a specific law from the Gemini API.

    Args:
        law_name (str): The name of the law to fetch details for.
        api_key (str): The Gemini API key.

    Returns:
        dict: The response from the Gemini API containing law details.
    """
    url = "https://gemini.api/endpoint"  # Replace with actual Gemini API endpoint

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "query": law_name,
        "context": "Legal Information",
        "fields": ["description", "applications", "precedents"]  # Example fields
    }

    try:
        # Make the request to the Gemini API using httpx asynchronously
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            return response.json()  # Return the response as a dictionary
        else:
            return {"error": f"Failed to fetch law details. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": f"An exception occurred: {str(e)}"}

# POST API for /knowlaw
@router.post("/knowlaw")
async def know_law(detail: LawDetail, db: AsyncSession = Depends(get_db)):
    """
    Endpoint to process law details and fetch additional information from an external API.
    """
    try:
        text_input = detail.text
        
        # Call the external API (local service running on port 8080)
        async with httpx.AsyncClient() as client:
            response = await client.get(f"http://localhost:8080/question/{text_input}")
        
        # Check if the request to the external API was successful
        if response.status_code == 200:
            # Parse the response from the external API
            external_response = response.json()

            # Fetch the Gemini API key from environment variables
            gem_api_key = os.getenv("GEM")

            if not gem_api_key:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Gemini API key not set")

            # Fetch law details from the Gemini API
            gem_data = await fetch_law_details_from_gemini(external_response["message"], gem_api_key)

            # Return the external response and the details from the Gemini API
            return {"message": external_response["message"], "Details": gem_data}

        else:
            raise HTTPException(status_code=response.status_code, detail="Error calling external API")

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"An error occurred: {str(e)}")