from fastapi import Request
from fastapi.responses import RedirectResponse
from jose import JWTError
from app.auth import verify_access_token
import os

async def auth_middleware(request: Request, call_next):
    # Skip the `/auth` routes
    if request.url.path.startswith("/auth"):
        return await call_next(request)
    
    # Get the token from cookies (or session)
    token = request.cookies.get("access_token")
    
    if token:
        payload = verify_access_token(token)
        if not payload:
            return RedirectResponse(url=f"{os.getenv('DOMAIN')}/login")
    else:
        return RedirectResponse(url=f"{os.getenv('DOMAIN')}/login")
    
    # Call the next middleware or route handler
    response = await call_next(request)
    return response
