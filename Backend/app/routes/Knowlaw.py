from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from pydantic import BaseModel
import os
import httpx
import asyncio

router = APIRouter()

class LawDetail(BaseModel):
    text: str

# Function to generate law explanation from the Gemini API
async def explain_law_from_text(text_chunk: str, api_key: str, retry_count: int = 3):
    """
    Explains the law based on the provided text using the Gemini API.
    Args:
        text_chunk (str): The text chunk for explaining the law.
        api_key (str): Gemini API key for authentication.
        retry_count (int): Number of times to retry on failure.
    Returns:
        str: A law explanation if successful, None otherwise.
    """
    prompt = f"""
    Your task is to read and understand the following legal text and provide a clear, concise explanation of the law described in the text. The explanation should focus on the key concepts and legal principles covered.

    Text: "{text_chunk}"

    Please provide the explanation in a concise and easy-to-understand format.
    """
    
    api_url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}'
    headers = {'Content-Type': 'application/json'}
    body = {"contents": [{"role": "user", "parts": [{"text": prompt}]}]}

    for attempt in range(retry_count):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(api_url, headers=headers, json=body)
                response.raise_for_status()
                data = response.json()

                # Parse the content for the explanation
                content = data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
                if content:
                    return content.strip()
                else:
                    return None

        except httpx.HTTPStatusError as e:
            print(f"HTTP error occurred: {e}")
            await asyncio.sleep(2)
        except Exception as e:
            print(f"An exception occurred: {str(e)}")
            await asyncio.sleep(2)

    return None


# POST API for /knowlaw
@router.post("/knowlaw")
async def know_law(detail: LawDetail, db: AsyncSession = Depends(get_db)):
    """
    Endpoint to process law details and fetch an explanation of the law from the Gemini API.
    """
    try:
        text_input = detail.text

        # Call the local API (example: http://localhost:8080/question/{text_input})
        async with httpx.AsyncClient() as client:
            response = await client.get(f"http://localhost:8080/model1/{text_input}")

        # Check if the local API request was successful
        if response.status_code == 200:
            # Parse the response from the local API
            external_response = response.json()
            law_text = external_response.get("message")
            print(law_text)
            if not law_text:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid response from local API")

            # Fetch the Gemini API key from environment variables
            gem_api_key = os.getenv("GEM")

            if not gem_api_key:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Gemini API key not set")

            # Call the Gemini API to explain the law based on the text
            law_explanation = await explain_law_from_text(law_text, gem_api_key)

            if law_explanation:
                print(law_explanation)
                return {"Law": law_text, "Explanation": law_explanation}
            else:
                return {"message": "Could not generate explanation from Gemini API"}

        else:
            raise HTTPException(status_code=response.status_code, detail="Error calling local API")

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"An error occurred: {str(e)}")