from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
import requests  # Replaced httpx with requests

router = APIRouter()

class LawDetail(BaseModel):
    text: str

@router.post("/analyze")
async def analyze_law(detail: LawDetail):
    """
    Sends the provided text to the local API and returns the response.
    """
    try:
        text_input = detail.text
        print(f"Received text input: {text_input}")

        # Call the local API using requests (example: http://localhost:8080/model2/{text_input})
        response = requests.get(f"http://localhost:8080/model2/{text_input}")
        print(f"Response status code from local API: {response.status_code}")

        # Check if the local API request was successful
        if response.status_code == 200:
            external_response = response.json()
            law_text = external_response.get("message")  # Corrected the way to access the message
            print(f"Response from local API: {law_text}")
            return external_response  # Return the entire response from the local API
        else:
            print(f"Error: Local API returned status code {response.status_code} with message {response.text}")
            raise HTTPException(status_code=response.status_code, detail="Error calling local API")

    except requests.RequestException as req_err:
        print(f"Request error occurred while calling the local API: {req_err}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Request error while calling local API")

    except ValueError as val_err:
        print(f"Value error occurred while parsing the local API response: {val_err}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Invalid response from local API")

    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"An error occurred: {str(e)}")