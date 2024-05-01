import beanie
import motor 
import motor.motor_asyncio
from user.model import User
from faculty.model import Faculty

async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://localhost:27017/TIP"
    )

    await beanie.init_beanie(
        database=client.db_name,
        document_models=[User, Faculty]
    )


# async def app_init():
#    client = motor.motor_asyncio.AsyncIOMotorClient(Settings().mongodb_url)
#    init_beanie(client.get_default_database(), document_models=[Cocktail])
#    app.include_router(cocktail_router, prefix="/v1")