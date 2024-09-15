from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routes import user_routes

app = FastAPI()

# Create database tables automatically
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Include user-related routes
app.include_router(user_routes.router, prefix="/auth")
