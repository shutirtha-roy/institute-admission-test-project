import bcrypt
import beanie
import motor 
import motor.motor_asyncio
from user.model import User, UserTypeEnum
from faculty.model import Faculty

async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://localhost:27017"
    )

    await beanie.init_beanie(
        database=client.instatuteDB,
        document_models=[User, Faculty]
    )

    admin = await User.find_one(User.email == "admin@gmail.com")

    if (admin == None):
        admin = User(
        name= "admin",
        email= "admin@gmail.com",
        password= "admin@gmail.com",
        role= UserTypeEnum.ADMIN,
        approved= True
    )
        
    admin.password = bcrypt.hashpw(
                admin.password.encode("utf-8"), bcrypt.gensalt())

    await admin.save()


# async def app_init():
#    client = motor.motor_asyncio.AsyncIOMotorClient(Settings().mongodb_url)
#    init_beanie(client.get_default_database(), document_models=[Cocktail])
#    app.include_router(cocktail_router, prefix="/v1")