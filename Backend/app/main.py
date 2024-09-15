from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routes import user_routes, auth_routes, account_routes
from app.middleware import auth_middleware
import os

app = FastAPI()

# Apply the middleware globally, but it will skip `/auth` routes
app.middleware("http")(auth_middleware)

# Create database tables automatically
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Include user-related routes under /auth
app.include_router(auth_routes.router, prefix="/auth")

# Include other user-related routes (require authentication)
app.include_router(user_routes.router)

# Include account-related routes under /account (require authentication)
app.include_router(account_routes.router, prefix="/account")
