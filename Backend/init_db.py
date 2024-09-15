# In the Python shell or a new script
from app.database import engine
from app.models import Base

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Call this function to initialize the tables
import asyncio
asyncio.run(init_db())
